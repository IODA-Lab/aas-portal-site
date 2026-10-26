(function () {
  'use strict';
  const DATA = JSON.parse(document.getElementById('portal-data').textContent);
  const EQ = Object.fromEntries(DATA.equipment.map(e => [e.no, e]));
  const KIND = Object.fromEntries(DATA.kinds.map(k => [k.id, k]));
  const DOCUMENTS = ['aasx', 'guidance', 'plan', 'review'];
  const MEDIA = ['video', 'simulator'];
  const PATHS = {
    grid:'M3 3h7v7H3zM14 3h7v7h-7zM3 14h7v7H3zM14 14h7v7h-7z',
    aasx:'m12 2 9 5v10l-9 5-9-5V7Zm0 10 9-5M12 12 3 7m9 5v10',
    guidance:'M3 4h6a4 4 0 0 1 3 2 4 4 0 0 1 3-2h6v15h-6a4 4 0 0 0-3 2 4 4 0 0 0-3-2H3Zm9 2v15',
    plan:'M6 2h9l4 4v16H6Zm8 0v5h5M9 11h7M9 15h7',
    review:'m12 2 8 3v6c0 5-5 9-8 11-3-2-8-6-8-11V5Zm-4 9 3 3 5-6',
    simulator:'M2 4h20v14H2Zm5 18h10M12 18v4M7 11h3l2-4 2 8 2-4h2',
    video:'M4 3h16v18H4Zm5 5 7 4-7 4Z',
    tool:'m14 3-3 6 4 4 6-3a7 7 0 0 1-9 8l-6 5-5-5 6-6a7 7 0 0 1 7-9Z',
    arrow:'M5 12h14m-5-5 5 5-5 5',
    search:'M16 16 22 22M18 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0',
    folder:'M3 5h6l2 3h10v12H3Z',
    external:'M14 3h7v7m0-7L10 14M9 3H3v18h18v-6'
  };
  function el(tag, attrs, ...children) {
    const n = document.createElement(tag);
    Object.entries(attrs || {}).forEach(([key, value]) => {
      if (value != null && value !== false) n.setAttribute(key, value === true ? '' : String(value));
    });
    children.flat(Infinity).forEach(child => {
      if (child != null && child !== false) n.append(child instanceof Node ? child : String(child));
    });
    return n;
  }
  function icon(name) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    Object.entries({viewBox:'0 0 24 24', fill:'none', stroke:'currentColor', 'stroke-width':'1.6', 'stroke-linecap':'round', 'stroke-linejoin':'round', 'aria-hidden':'true', class:'icon'}).forEach(([k,v]) => svg.setAttribute(k,v));
    const path = document.createElementNS(svg.namespaceURI, 'path');
    path.setAttribute('d', PATHS[name] || PATHS.folder); svg.append(path); return svg;
  }
  const eqLink = no => '#/equipment/' + no;
  const itemsOf = no => DATA.items.filter(i => i.equipment === no);
  const label = id => KIND[id].label;
  const byName = (a,b) => a.name.localeCompare(b.name, 'ko');
  function breadcrumbs(parts) {
    return el('nav', {class:'breadcrumbs', 'aria-label':'현재 위치'}, el('a', {href:'#/'}, '장비별 산출물'), parts.map(p => [el('span', {'aria-hidden':'true'}, '/'), el('span', {'aria-current':'page'}, p)]));
  }
  function pageHead(title, detail) {
    return el('header', {class:'page-head'}, el('h1', null, title), detail ? el('p', null, detail) : null);
  }
  function empty() {
    return el('div', {class:'empty-state'}, icon('folder'), el('p', null, '등록된 자료가 없습니다.'));
  }
  function table(headers, body, className) {
    return el('div', {class:'table-wrap'}, el('table', {class:className || 'resource-table'},
      el('thead', null, el('tr', null, headers.map(h => el('th', {scope:'col'}, h)))), body));
  }
  function availableCount(items, kinds) {
    const count = items.filter(i => kinds.includes(i.kind) && i.href).length;
    return count ? el('span', {class:'file-count'}, count) : el('span', {class:'dash', 'aria-label':'등록된 자료 없음'}, '—');
  }
  function all(params) {
    const state = {q:params.q || '', group:params.group || '', limit:20};
    const query = el('input', {id:'equipment-search', type:'search', placeholder:'장비명 검색', value:state.q, autocomplete:'off'});
    const groups = [...new Set(DATA.equipment.map(e => e.group))].sort((a,b) => a.localeCompare(b,'ko'));
    const select = el('select', {id:'group-filter'}, el('option', {value:''}, '모든 장비 분류'), groups.map(g => el('option', {value:g, selected:state.group===g}, g)));
    const reset = el('button', {type:'button', class:'text-button'}, '초기화');
    const body = el('tbody');
    const count = el('span', {class:'result-count', 'aria-live':'polite'});
    const more = el('button', {type:'button', class:'button'}, '더 보기');
    function refresh() {
      const q = state.q.trim().toLocaleLowerCase();
      const list = DATA.equipment.filter(e => (!state.group || e.group===state.group) && (!q || (e.name+' '+(e.name_en||'')+' '+e.group+' '+e.no).toLocaleLowerCase().includes(q))).sort(byName);
      body.replaceChildren(...list.slice(0,state.limit).map(e => {
        const items = itemsOf(e.no);
        return el('tr', null,
          el('td', {class:'equipment-name'}, el('a', {href:eqLink(e.no)}, icon('aasx'), el('span', null, e.name))),
          el('td', {class:'equipment-group'}, e.group),
          el('td', {class:'count-cell'}, availableCount(items,['aasx'])),
          el('td', {class:'count-cell'}, availableCount(items,['guidance','plan','review'])),
          el('td', {class:'count-cell'}, availableCount(items,['video','simulator','tool'])),
          el('td', {class:'row-arrow'}, el('a', {href:eqLink(e.no), 'aria-label':e.name+' 상세 보기'}, icon('arrow'))));
      }));
      if (!list.length) body.append(el('tr', null, el('td', {colspan:6}, el('div', {class:'empty-state'}, icon('search'), el('p', null, '검색 결과가 없습니다.')))));
      count.textContent = '장비 '+list.length+'개';
      more.hidden = state.limit >= list.length;
      more.textContent = '더 보기 ('+Math.min(state.limit,list.length)+' / '+list.length+')';
      reset.hidden = !state.q && !state.group;
      const p = new URLSearchParams(); if(state.q)p.set('q',state.q); if(state.group)p.set('group',state.group);
      history.replaceState(null,'','#/all'+(p.size?'?'+p.toString():''));
    }
    query.addEventListener('input',()=>{state.q=query.value;state.limit=20;refresh();});
    select.addEventListener('change',()=>{state.group=select.value;state.limit=20;refresh();});
    reset.addEventListener('click',()=>{state.q='';state.group='';state.limit=20;query.value='';select.value='';refresh();query.focus();});
    more.addEventListener('click',()=>{const start=state.limit;state.limit+=20;refresh();body.children[start]?.querySelector('a')?.focus();});
    refresh();
    return [pageHead('장비별 산출물'),
      el('div', {class:'catalog-tools'}, el('div', {class:'search-field'}, el('label', {for:'equipment-search', class:'sr-only'}, '장비 검색'), icon('search'), query),
        el('label', {for:'group-filter', class:'sr-only'}, '장비 분류'), select),
      el('div', {class:'list-caption'}, count, reset, DATA.items.length===0 ? el('span', {class:'muted'}, '산출물 미등록') : null),
      table(['장비명','장비 분류','참조모델','문서','영상·도구',''],body,'equipment-table'),
      el('div', {class:'load-more'},more)];
  }
  function action(i) {
    if (!i.href) return el('span', {class:'muted'}, '—');
    return el('a', {class:'file-link', href:i.href, target:'_blank', rel:'noopener'}, i.kind==='video'?'영상 보기':i.external?'열기':'다운로드',icon('external'));
  }
  function itemRow(i, showEquipment) {
    return el('tr', null,
      el('td', {class:'resource-name'}, el('strong', null, i.variant || i.title), i.file_name ? el('small', null, i.file_name) : null),
      showEquipment ? el('td', null, EQ[i.equipment] ? el('a', {href:eqLink(i.equipment)}, EQ[i.equipment].name) : '공통') : null,
      el('td', {class:'version-cell'}, i.version || '—'), el('td', {class:'date-cell'}, i.version_date || i.modified || '—'), el('td', null, action(i)));
  }
  function resourceTable(items, options) {
    const showEquipment = options?.showEquipment;
    const slots = options?.slots || [];
    const headers = ['자료명', ...(showEquipment?['장비']:[]), '버전', '날짜', '파일'];
    const body = el('tbody');
    if (slots.length) {
      slots.forEach(k => {
        const subset = items.filter(i => i.kind===k);
        if(subset.length) body.append(...subset.map(i=>itemRow(i,false)));
        else body.append(el('tr', {class:'empty-slot'}, el('td', {class:'slot-label'}, icon(k),label(k)), el('td', null,'—'),el('td',null,'—'),el('td',null,el('span',{class:'muted'},'미등록'))));
      });
    } else if(items.length) body.append(...items.map(i=>itemRow(i,showEquipment)));
    else body.append(el('tr', null, el('td', {colspan:headers.length},empty())));
    return table(headers,body);
  }
  function videoList(items) {
    return el('div', {class:'video-list'}, items.map(i => el('article', {class:'video-card'},
      i.play_src ? el('video', {controls:true,preload:'metadata',src:i.play_src,'aria-label':i.title}) : null,
      el('div', {class:'video-info'}, el('h2',null,i.title), action(i)))));
  }
  function equipment(no,params) {
    const e=EQ[no]; if(!e)return notFound();
    const tab=['resources','media','tools'].includes(params.tab)?params.tab:'resources';
    const kinds=tab==='resources'?DOCUMENTS:tab==='media'?MEDIA:['tool'];
    const items=itemsOf(no).filter(i=>kinds.includes(i.kind));
    return [breadcrumbs([e.name]),pageHead(e.name,e.group),
      el('nav', {class:'detail-tabs','aria-label':'장비 자료 구분'}, [['resources','모델·문서'],['media','영상·시뮬레이터'],['tools','변환기·도구']].map(([id,title])=>el('a',{href:eqLink(no)+'?tab='+id,'aria-current':tab===id?'page':null},title))),
      tab==='media'&&items.some(i=>i.play_src)?videoList(items.filter(i=>i.kind==='video')):null,
      resourceTable(items,{slots:kinds})];
  }
  function kind(id) {
    if(!KIND[id])return notFound();
    const items=DATA.items.filter(i=>i.kind===id);
    return [breadcrumbs([label(id)]),pageHead(label(id)),
      el('div',{class:'list-caption'},el('span',null,'자료 '+items.length+'건')),
      id==='video'&&items.some(i=>i.play_src)?videoList(items):null,
      resourceTable(items,{showEquipment:true})];
  }
  function notFound() {
    return [pageHead('페이지를 찾을 수 없습니다.'),el('a',{class:'button',href:'#/'},'장비별 산출물로 돌아가기')];
  }
  function sidebar() {
    const nav=document.getElementById('navigation');
    const link=(title,href,name)=>el('a',{href},icon(name),el('span',null,title));
    nav.append(link('장비별 산출물','#/all','grid'),
      el('div',{class:'nav-section'},el('span',{class:'nav-heading'},'모델·문서'),DOCUMENTS.map(k=>link(label(k),'#/kind/'+k,k))),
      el('div',{class:'nav-section'},el('span',{class:'nav-heading'},'영상·프로그램'),[...MEDIA,'tool'].map(k=>link(label(k),'#/kind/'+k,k))));
  }
  function setMenu(open) {
    document.body.classList.toggle('nav-open',open);
    const btn=document.querySelector('.menu-btn');
    btn.setAttribute('aria-expanded',String(open));btn.setAttribute('aria-label',open?'메뉴 닫기':'메뉴 열기');
    document.querySelector('.nav-backdrop').hidden=!open;
    document.getElementById('sidebar').inert=window.matchMedia('(max-width:760px)').matches&&!open;
    if(open)(document.querySelector('#navigation a[aria-current]')||document.querySelector('.nav-close')).focus();
  }
  function render() {
    const hash=location.hash.replace(/^#\/?/,''), split=hash.indexOf('?'), raw=split<0?hash:hash.slice(0,split);
    let parts;try{parts=raw.split('/').filter(Boolean).map(decodeURIComponent);}catch{parts=['invalid'];}
    const params=Object.fromEntries(new URLSearchParams(split<0?'':hash.slice(split+1))), [route,id]=parts;
    const content=!route||route==='all'?all(params):route==='equipment'?equipment(Number(id),params):route==='kind'?kind(id):notFound();
    const main=document.getElementById('main');main.replaceChildren(...content.filter(Boolean));
    for(const a of document.querySelectorAll('#navigation a')){
      const current=a.getAttribute('href'), match=current==='#/'+raw||((!route||route==='equipment')&&current==='#/all');
      if(match)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');
    }
    document.title=main.querySelector('h1').textContent+' · '+DATA.meta.title;
    setMenu(false);window.scrollTo(0,0);main.focus({preventScroll:true});
  }
  sidebar();
  document.querySelector('.menu-btn').addEventListener('click',()=>setMenu(!document.body.classList.contains('nav-open')));
  document.querySelectorAll('.nav-close,.nav-backdrop').forEach(button=>button.addEventListener('click',()=>{setMenu(false);document.querySelector('.menu-btn').focus();}));
  window.matchMedia('(max-width:760px)').addEventListener('change',()=>setMenu(false));
  document.addEventListener('keydown',event=>{
    if(!document.body.classList.contains('nav-open'))return;
    if(event.key==='Escape'){setMenu(false);document.querySelector('.menu-btn').focus();}
    if(event.key==='Tab'){
      const controls=[...document.querySelectorAll('#sidebar a,#sidebar button')],first=controls[0],last=controls[controls.length-1];
      if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}
      else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}
    }
  });
  document.querySelector('.skip').addEventListener('click',event=>{event.preventDefault();document.getElementById('main').focus();});
  window.addEventListener('hashchange',render);render();
})();
