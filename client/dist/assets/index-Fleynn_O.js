(function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const i of document.querySelectorAll('link[rel="modulepreload"]'))n(i);new MutationObserver(i=>{for(const l of i)if(l.type==="childList")for(const o of l.addedNodes)o.tagName==="LINK"&&o.rel==="modulepreload"&&n(o)}).observe(document,{childList:!0,subtree:!0});function r(i){const l={};return i.integrity&&(l.integrity=i.integrity),i.referrerPolicy&&(l.referrerPolicy=i.referrerPolicy),i.crossOrigin==="use-credentials"?l.credentials="include":i.crossOrigin==="anonymous"?l.credentials="omit":l.credentials="same-origin",l}function n(i){if(i.ep)return;i.ep=!0;const l=r(i);fetch(i.href,l)}})();const Tt=!1;var xt=Array.isArray,Nt=Array.from,kt=Object.defineProperty,ce=Object.getOwnPropertyDescriptor,Ge=Object.getOwnPropertyDescriptors,_e=Object.getPrototypeOf;function St(e){return e()}function ve(e){for(var t=0;t<e.length;t++)e[t]()}const D=2,Ue=4,z=8,Ee=16,k=32,J=64,F=128,ne=256,b=512,L=1024,Q=2048,j=4096,X=8192,Pt=16384,be=32768,Ct=65536,At=1<<18,We=1<<19,de=Symbol("$state"),Ot=Symbol("legacy props"),Dt=Symbol("");function Ke(e){return e===this.v}function Rt(e,t){return e!=e?t==t:e!==t||e!==null&&typeof e=="object"||typeof e=="function"}function ze(e){return!Rt(e,this.v)}function Lt(e){throw new Error("effect_in_teardown")}function Bt(){throw new Error("effect_in_unowned_derived")}function Ft(e){throw new Error("effect_orphan")}function It(){throw new Error("effect_update_depth_exceeded")}function qt(e){throw new Error("props_invalid_value")}function Mt(){throw new Error("state_unsafe_local_read")}function jt(){throw new Error("state_unsafe_mutation")}let $=!1;function $t(){$=!0}function Je(e){return{f:0,v:e,reactions:null,equals:Ke,version:0}}function Vt(e,t=!1){var n;const r=Je(e);return t||(r.equals=ze),$&&h!==null&&h.l!==null&&((n=h.l).s??(n.s=[])).push(r),r}function Yt(e,t=!1){return Ht(Vt(e,t))}function Ht(e){return d!==null&&d.f&D&&(C===null?ur([e]):C.push(e)),e}function Ae(e,t){return d!==null&&Pe()&&d.f&(D|Ee)&&(C===null||!C.includes(e))&&jt(),Gt(e,t)}function Gt(e,t){return e.equals(t)||(e.v=t,e.version=ht(),Qe(e,L),Pe()&&c!==null&&c.f&b&&!(c.f&k)&&(y!==null&&y.includes(e)?(O(c,L),se(c)):R===null?fr([e]):R.push(e))),t}function Qe(e,t){var r=e.reactions;if(r!==null)for(var n=Pe(),i=r.length,l=0;l<i;l++){var o=r[l],a=o.f;a&L||!n&&o===c||(O(o,t),a&(b|F)&&(a&D?Qe(o,Q):se(o)))}}const Ut=1,Wt=2,Kt=8,zt=1,Jt=2;let Qt=!1;var Oe,Xe,Ze;function Xt(){if(Oe===void 0){Oe=window;var e=Element.prototype,t=Node.prototype;Xe=ce(t,"firstChild").get,Ze=ce(t,"nextSibling").get,e.__click=void 0,e.__className="",e.__attributes=null,e.__styles=null,e.__e=void 0,Text.prototype.__t=void 0}}function Te(e=""){return document.createTextNode(e)}function ie(e){return Xe.call(e)}function xe(e){return Ze.call(e)}function E(e,t){return ie(e)}function et(e,t){{var r=ie(e);return r instanceof Comment&&r.data===""?xe(r):r}}function N(e,t=1,r=!1){let n=e;for(;t--;)n=xe(n);return n}function Ne(e){var t=D|L;c===null?t|=F:c.f|=We;const r={children:null,ctx:h,deps:null,equals:Ke,f:t,fn:e,reactions:null,v:null,version:0,parent:c};if(d!==null&&d.f&D){var n=d;(n.children??(n.children=[])).push(r)}return r}function Zt(e){const t=Ne(e);return t.equals=ze,t}function tt(e){var t=e.children;if(t!==null){e.children=null;for(var r=0;r<t.length;r+=1){var n=t[r];n.f&D?ke(n):Y(n)}}}function rt(e){var t,r=c;A(e.parent);try{tt(e),t=pt(e)}finally{A(r)}return t}function nt(e){var t=rt(e),r=(q||e.f&F)&&e.deps!==null?Q:b;O(e,r),e.equals(t)||(e.v=t,e.version=ht())}function ke(e){tt(e),W(e,0),O(e,X),e.v=e.children=e.deps=e.ctx=e.reactions=null}function it(e){c===null&&d===null&&Ft(),d!==null&&d.f&F&&Bt(),Se&&Lt()}function er(e,t){var r=t.last;r===null?t.last=t.first=e:(r.next=e,e.prev=r,t.last=e)}function V(e,t,r,n=!0){var i=(e&J)!==0,l=c,o={ctx:h,deps:null,deriveds:null,nodes_start:null,nodes_end:null,f:e|L,first:null,fn:t,last:null,next:null,parent:i?null:l,prev:null,teardown:null,transitions:null,version:0};if(r){var a=M;try{Le(!0),ae(o),o.f|=Pt}catch(v){throw Y(o),v}finally{Le(a)}}else t!==null&&se(o);var s=r&&o.deps===null&&o.first===null&&o.nodes_start===null&&o.teardown===null&&(o.f&We)===0;if(!s&&!i&&n&&(l!==null&&er(o,l),d!==null&&d.f&D)){var f=d;(f.children??(f.children=[])).push(o)}return o}function tr(e){const t=V(z,null,!1);return O(t,b),t.teardown=e,t}function he(e){it();var t=c!==null&&(c.f&k)!==0&&h!==null&&!h.m;if(t){var r=h;(r.e??(r.e=[])).push({fn:e,effect:c,reaction:d})}else{var n=lt(e);return n}}function rr(e){return it(),ot(e)}function nr(e){const t=V(J,e,!0);return()=>{Y(t)}}function lt(e){return V(Ue,e,!1)}function ot(e){return V(z,e,!0)}function U(e){return at(e)}function at(e,t=0){return V(z|Ee|t,e,!0)}function pe(e,t=!0){return V(z|k,e,!0,t)}function st(e){var t=e.teardown;if(t!==null){const r=Se,n=d;Be(!0),B(null);try{t.call(null)}finally{Be(r),B(n)}}}function ut(e){var t=e.deriveds;if(t!==null){e.deriveds=null;for(var r=0;r<t.length;r+=1)ke(t[r])}}function ft(e,t=!1){var r=e.first;for(e.first=e.last=null;r!==null;){var n=r.next;Y(r,t),r=n}}function ir(e){for(var t=e.first;t!==null;){var r=t.next;t.f&k||Y(t),t=r}}function Y(e,t=!0){var r=!1;if((t||e.f&At)&&e.nodes_start!==null){for(var n=e.nodes_start,i=e.nodes_end;n!==null;){var l=n===i?null:xe(n);n.remove(),n=l}r=!0}ft(e,t&&!r),ut(e),W(e,0),O(e,X);var o=e.transitions;if(o!==null)for(const s of o)s.stop();st(e);var a=e.parent;a!==null&&a.first!==null&&ct(e),e.next=e.prev=e.teardown=e.ctx=e.deps=e.parent=e.fn=e.nodes_start=e.nodes_end=null}function ct(e){var t=e.parent,r=e.prev,n=e.next;r!==null&&(r.next=n),n!==null&&(n.prev=r),t!==null&&(t.first===e&&(t.first=n),t.last===e&&(t.last=r))}function De(e,t){var r=[];_t(e,r,!0),lr(r,()=>{Y(e),t&&t()})}function lr(e,t){var r=e.length;if(r>0){var n=()=>--r||t();for(var i of e)i.out(n)}else t()}function _t(e,t,r){if(!(e.f&j)){if(e.f^=j,e.transitions!==null)for(const o of e.transitions)(o.is_global||r)&&t.push(o);for(var n=e.first;n!==null;){var i=n.next,l=(n.f&be)!==0||(n.f&k)!==0;_t(n,t,l?r:!1),n=i}}}function Re(e){vt(e,!0)}function vt(e,t){if(e.f&j){Z(e)&&ae(e),e.f^=j;for(var r=e.first;r!==null;){var n=r.next,i=(r.f&be)!==0||(r.f&k)!==0;vt(r,i?t:!1),r=n}if(e.transitions!==null)for(const l of e.transitions)(l.is_global||t)&&l.in()}}let me=!1,ge=[];function or(){me=!1;const e=ge.slice();ge=[],ve(e)}function ar(e){me||(me=!0,queueMicrotask(or)),ge.push(e)}function sr(e){throw new Error("lifecycle_outside_component")}let le=!1,M=!1,Se=!1;function Le(e){M=e}function Be(e){Se=e}let we=[],G=0;let d=null;function B(e){d=e}let c=null;function A(e){c=e}let C=null;function ur(e){C=e}let y=null,x=0,R=null;function fr(e){R=e}let dt=0,q=!1,h=null;function ht(){return++dt}function Pe(){return!$||h!==null&&h.l===null}function Z(e){var o,a;var t=e.f;if(t&L)return!0;if(t&Q){var r=e.deps,n=(t&F)!==0;if(r!==null){var i;if(t&ne){for(i=0;i<r.length;i++)((o=r[i]).reactions??(o.reactions=[])).push(e);e.f^=ne}for(i=0;i<r.length;i++){var l=r[i];if(Z(l)&&nt(l),n&&c!==null&&!q&&!((a=l==null?void 0:l.reactions)!=null&&a.includes(e))&&(l.reactions??(l.reactions=[])).push(e),l.version>e.version)return!0}}n||O(e,b)}return!1}function cr(e,t,r){throw e}function pt(e){var _;var t=y,r=x,n=R,i=d,l=q,o=C,a=h,s=e.f;y=null,x=0,R=null,d=s&(k|J)?null:e,q=!M&&(s&F)!==0,C=null,h=e.ctx;try{var f=(0,e.fn)(),v=e.deps;if(y!==null){var u;if(W(e,x),v!==null&&x>0)for(v.length=x+y.length,u=0;u<y.length;u++)v[x+u]=y[u];else e.deps=v=y;if(!q)for(u=x;u<v.length;u++)((_=v[u]).reactions??(_.reactions=[])).push(e)}else v!==null&&x<v.length&&(W(e,x),v.length=x);return f}finally{y=t,x=r,R=n,d=i,q=l,C=o,h=a}}function _r(e,t){let r=t.reactions;if(r!==null){var n=r.indexOf(e);if(n!==-1){var i=r.length-1;i===0?r=t.reactions=null:(r[n]=r[i],r.pop())}}r===null&&t.f&D&&(y===null||!y.includes(t))&&(O(t,Q),t.f&(F|ne)||(t.f^=ne),W(t,0))}function W(e,t){var r=e.deps;if(r!==null)for(var n=t;n<r.length;n++)_r(e,r[n])}function ae(e){var t=e.f;if(!(t&X)){O(e,b);var r=c;c=e;try{t&Ee?ir(e):ft(e),ut(e),st(e);var n=pt(e);e.teardown=typeof n=="function"?n:null,e.version=dt}catch(i){cr(i)}finally{c=r}}}function vr(){G>1e3&&(G=0,It()),G++}function dr(e){var t=e.length;if(t!==0){vr();var r=M;M=!0;try{for(var n=0;n<t;n++){var i=e[n];i.f&b||(i.f^=b);var l=[];mt(i,l),hr(l)}}finally{M=r}}}function hr(e){var t=e.length;if(t!==0)for(var r=0;r<t;r++){var n=e[r];!(n.f&(X|j))&&Z(n)&&(ae(n),n.deps===null&&n.first===null&&n.nodes_start===null&&(n.teardown===null?ct(n):n.fn=null))}}function pr(){if(le=!1,G>1001)return;const e=we;we=[],dr(e),le||(G=0)}function se(e){le||(le=!0,queueMicrotask(pr));for(var t=e;t.parent!==null;){t=t.parent;var r=t.f;if(r&(J|k)){if(!(r&b))return;t.f^=b}}we.push(t)}function mt(e,t){var r=e.first,n=[];e:for(;r!==null;){var i=r.f,l=(i&k)!==0,o=l&&(i&b)!==0;if(!o&&!(i&j))if(i&z){l?r.f^=b:Z(r)&&ae(r);var a=r.first;if(a!==null){r=a;continue}}else i&Ue&&n.push(r);var s=r.next;if(s===null){let u=r.parent;for(;u!==null;){if(e===u)break e;var f=u.next;if(f!==null){r=f;continue e}u=u.parent}}r=s}for(var v=0;v<n.length;v++)a=n[v],t.push(a),mt(a,t)}function K(e){var a;var t=e.f,r=(t&D)!==0;if(r&&t&X){var n=rt(e);return ke(e),n}if(d!==null){C!==null&&C.includes(e)&&Mt();var i=d.deps;y===null&&i!==null&&i[x]===e?x++:y===null?y=[e]:y.push(e),R!==null&&c!==null&&c.f&b&&!(c.f&k)&&R.includes(e)&&(O(c,L),se(c))}else if(r&&e.deps===null){var l=e,o=l.parent;o!==null&&!((a=o.deriveds)!=null&&a.includes(l))&&(o.deriveds??(o.deriveds=[])).push(l)}return r&&(l=e,Z(l)&&nt(l)),e.v}function gt(e){const t=d;try{return d=null,e()}finally{d=t}}const mr=~(L|Q|b);function O(e,t){e.f=e.f&mr|t}function wt(e,t=!1,r){h={p:h,c:null,e:null,m:!1,s:e,x:null,l:null},$&&!t&&(h.l={s:null,u:null,r1:[],r2:Je(!1)})}function yt(e){const t=h;if(t!==null){const o=t.e;if(o!==null){var r=c,n=d;t.e=null;try{for(var i=0;i<o.length;i++){var l=o[i];A(l.effect),B(l.reaction),lt(l.fn)}}finally{A(r),B(n)}}h=t.p,t.m=!0}return{}}function gr(e){if(!(typeof e!="object"||!e||e instanceof EventTarget)){if(de in e)ye(e);else if(!Array.isArray(e))for(let t in e){const r=e[t];typeof r=="object"&&r&&de in r&&ye(r)}}}function ye(e,t=new Set){if(typeof e=="object"&&e!==null&&!(e instanceof EventTarget)&&!t.has(e)){t.add(e),e instanceof Date&&e.getTime();for(let n in e)try{ye(e[n],t)}catch{}const r=_e(e);if(r!==Object.prototype&&r!==Array.prototype&&r!==Map.prototype&&r!==Set.prototype&&r!==Date.prototype){const n=Ge(r);for(let i in n){const l=n[i].get;if(l)try{l.call(e)}catch{}}}}}let Fe=!1;function wr(){Fe||(Fe=!0,document.addEventListener("reset",e=>{Promise.resolve().then(()=>{var t;if(!e.defaultPrevented)for(const r of e.target.elements)(t=r.__on_r)==null||t.call(r)})},{capture:!0}))}function Et(e){var t=d,r=c;B(null),A(null);try{return e()}finally{B(t),A(r)}}function yr(e,t,r,n=r){e.addEventListener(t,()=>Et(r));const i=e.__on_r;i?e.__on_r=()=>{i(),n()}:e.__on_r=n,wr()}const Er=new Set,Ie=new Set;function br(e,t,r,n){function i(l){if(n.capture||H.call(t,l),!l.cancelBubble)return Et(()=>r.call(this,l))}return e.startsWith("pointer")||e.startsWith("touch")||e==="wheel"?ar(()=>{t.addEventListener(e,i,n)}):t.addEventListener(e,i,n),i}function Tr(e,t,r,n,i){var l={capture:n,passive:i},o=br(e,t,r,l);(t===document.body||t===window||t===document)&&tr(()=>{t.removeEventListener(e,o,l)})}function H(e){var Ce;var t=this,r=t.ownerDocument,n=e.type,i=((Ce=e.composedPath)==null?void 0:Ce.call(e))||[],l=i[0]||e.target,o=0,a=e.__root;if(a){var s=i.indexOf(a);if(s!==-1&&(t===document||t===window)){e.__root=t;return}var f=i.indexOf(t);if(f===-1)return;s<=f&&(o=s)}if(l=i[o]||e.target,l!==t){kt(e,"currentTarget",{configurable:!0,get(){return l||r}});var v=d,u=c;B(null),A(null);try{for(var _,p=[];l!==null;){var T=l.assignedSlot||l.parentNode||l.host||null;try{var S=l["__"+n];if(S!==void 0&&!l.disabled)if(xt(S)){var[ee,...P]=S;ee.apply(l,[e,...P])}else S.call(l,e)}catch(te){_?p.push(te):_=te}if(e.cancelBubble||T===t||T===null)break;l=T}if(_){for(let te of p)queueMicrotask(()=>{throw te});throw _}}finally{e.__root=t,delete e.currentTarget,B(v),A(u)}}}function xr(e){var t=document.createElement("template");return t.innerHTML=e,t.content}function oe(e,t){var r=c;r.nodes_start===null&&(r.nodes_start=e,r.nodes_end=t)}function w(e,t){var r=(t&zt)!==0,n=(t&Jt)!==0,i,l=!e.startsWith("<!>");return()=>{i===void 0&&(i=xr(l?e:"<!>"+e),r||(i=ie(i)));var o=n?document.importNode(i,!0):i.cloneNode(!0);if(r){var a=ie(o),s=o.lastChild;oe(a,s)}else oe(o,o);return o}}function qe(e=""){{var t=Te(e+"");return oe(t,t),t}}function Nr(){var e=document.createDocumentFragment(),t=document.createComment(""),r=Te();return e.append(t,r),oe(t,r),e}function m(e,t){e!==null&&e.before(t)}const kr=["touchstart","touchmove"];function Sr(e){return kr.includes(e)}function Me(e,t){var r=t==null?"":typeof t=="object"?t+"":t;r!==(e.__t??(e.__t=e.nodeValue))&&(e.__t=r,e.nodeValue=r==null?"":r+"")}function Pr(e,t){return Cr(e,t)}const I=new Map;function Cr(e,{target:t,anchor:r,props:n={},events:i,context:l,intro:o=!0}){Xt();var a=new Set,s=u=>{for(var _=0;_<u.length;_++){var p=u[_];if(!a.has(p)){a.add(p);var T=Sr(p);t.addEventListener(p,H,{passive:T});var S=I.get(p);S===void 0?(document.addEventListener(p,H,{passive:T}),I.set(p,1)):I.set(p,S+1)}}};s(Nt(Er)),Ie.add(s);var f=void 0,v=nr(()=>{var u=r??t.appendChild(Te());return pe(()=>{if(l){wt({});var _=h;_.c=l}i&&(n.$$events=i),f=e(u,n)||{},l&&yt()}),()=>{var T;for(var _ of a){t.removeEventListener(_,H);var p=I.get(_);--p===0?(document.removeEventListener(_,H),I.delete(_)):I.set(_,p)}Ie.delete(s),je.delete(f),u!==r&&((T=u.parentNode)==null||T.removeChild(u))}});return je.set(f,v),f}let je=new WeakMap;function Ar(e,t,r,n=null,i=!1){var l=e,o=null,a=null,s=null,f=i?be:0;at(()=>{s!==(s=!!t())&&(s?(o?Re(o):o=pe(()=>r(l)),a&&De(a,()=>{a=null})):(a?Re(a):n&&(a=pe(()=>n(l))),o&&De(o,()=>{o=null})))},f)}function $e(e,t,r,n,i){var a;var l=(a=t.$$slots)==null?void 0:a[r],o=!1;l===!0&&(l=t[r==="default"?"children":r],o=!0),l===void 0?i!==null&&i(e):l(e,o?()=>n:n)}function ue(e,t,r,n){var i=e.__attributes??(e.__attributes={});i[t]!==(i[t]=r)&&(t==="style"&&"__styles"in e&&(e.__styles={}),t==="loading"&&(e[Dt]=r),r==null?e.removeAttribute(t):typeof r!="string"&&Or(e).includes(t)?e[t]=r:e.setAttribute(t,r))}var Ve=new Map;function Or(e){var t=Ve.get(e.nodeName);if(t)return t;Ve.set(e.nodeName,t=[]);for(var r,n=_e(e),i=Element.prototype;i!==n;){r=Ge(n);for(var l in r)r[l].set&&t.push(l);n=_e(n)}return t}function Dr(e,t){var r=e.__className,n=Rr(t);(r!==n||Qt)&&(t==null?e.removeAttribute("class"):e.className=n,e.__className=n)}function Rr(e){return e??""}function Lr(e,t,r=t){yr(e,"change",()=>{var n=e.checked;r(n)}),t()==null&&r(!1),ot(()=>{var n=t();e.checked=!!n})}function Br(e=!1){const t=h,r=t.l.u;if(!r)return;let n=()=>gr(t.s);if(e){let i=0,l={};const o=Ne(()=>{let a=!1;const s=t.s;for(const f in s)s[f]!==l[f]&&(l[f]=s[f],a=!0);return a&&i++,i});n=()=>K(o)}r.b.length&&rr(()=>{Ye(t,n),ve(r.b)}),he(()=>{const i=gt(()=>r.m.map(St));return()=>{for(const l of i)typeof l=="function"&&l()}}),r.a.length&&he(()=>{Ye(t,n),ve(r.a)})}function Ye(e,t){if(e.l.s)for(const r of e.l.s)K(r);t()}let re=!1;function Fr(e){var t=re;try{return re=!1,[e(),re]}finally{re=t}}function Ir(e){for(var t=c,r=c;t!==null&&!(t.f&(k|J));)t=t.parent;try{return A(t),e()}finally{A(r)}}function g(e,t,r,n){var ee;var i=(r&Ut)!==0,l=!$||(r&Wt)!==0,o=(r&Kt)!==0,a=!1,s;[s,a]=Fr(()=>e[t]);var f=de in e||Ot in e,v=((ee=ce(e,t))==null?void 0:ee.set)??(f&&o&&t in e?P=>e[t]=P:void 0),u=n,_=!0,p=()=>(_&&(_=!1,u=n),u);s===void 0&&n!==void 0&&(v&&l&&qt(),s=p(),v&&v(s));var T;if(l)T=()=>{var P=e[t];return P===void 0?p():(_=!0,P)};else{var S=Ir(()=>(i?Ne:Zt)(()=>e[t]));S.f|=Ct,T=()=>{var P=K(S);return P!==void 0&&(u=void 0),P===void 0?u:P}}return T}function qr(e){h===null&&sr(),$&&h.l!==null?Mr(h).m.push(e):he(()=>{const t=gt(e);if(typeof t=="function")return t})}function Mr(e){var t=e.l;return t.u??(t.u={a:[],b:[],m:[]})}const jr="5";typeof window<"u"&&(window.__svelte||(window.__svelte={v:new Set})).v.add(jr);$t();var $r=w('<div><input type="checkbox" class="drawer-toggle"> <div class="drawer-content p-16 flex flex-col"><!></div> <div class="drawer-side flex-shrink-0 p-5"><!></div></div>');function He(e,t){let r=g(t,"isRightDrawer",8),n=r()?"drawer-end":"",i=r()?"right-drawer-toggle":"left-drawer-toggle";var l=$r();Dr(l,`drawer xl:drawer-open ${n??""}`);var o=E(l);ue(o,"id",i);var a=N(o,2),s=E(a);$e(s,t,"pageContent",{},u=>{var _=qe("if you see this, i messed up");m(u,_)});var f=N(a,2),v=E(f);$e(v,t,"drawerContent",{},u=>{var _=qe("if you see this, i messed up");m(u,_)}),m(e,l)}var Vr=w('<footer class="footer p-4 bg-base-300"><span>© 2024 Dr. Richard Brearton</span></footer>');function Yr(e){var t=Vr();m(e,t)}var Hr=w('<article class="prose px-5"><h4 class="text-primary-content"> </h4></article>'),Gr=w('<article class="prose"><h4 class="text-primary-content"> </h4></article>');function bt(e,t){let r=g(t,"title",8),n=g(t,"isPadded",8,!0);var i=Nr(),l=et(i);Ar(l,n,o=>{var a=Hr(),s=E(a),f=E(s);U(()=>Me(f,r())),m(o,a)},o=>{var a=Gr(),s=E(a),f=E(s);U(()=>Me(f,r())),m(o,a)}),m(e,i)}var Ur=w('<a class="btn btn-ghost"><!></a>');function fe(e,t){let r=g(t,"text",8),n=g(t,"route",8);var i=Ur(),l=E(i);bt(l,{get title(){return r()},isPadded:!1}),U(()=>ue(i,"href",n())),m(e,i)}var Wr=w('<div class="navbar-center"><!> <!> <!></div>');function Kr(e){var t=Wr(),r=E(t);fe(r,{text:"Home",route:"/"});var n=N(r,2);fe(n,{text:"Physics",route:"/physics"});var i=N(n,2);fe(i,{text:"Research",route:"/research"}),m(e,t)}var zr=w('<a class="px-5 text-primary-content" aria-label="Github link"><svg width="32" height="32" viewBox="0 0 16 16" version="1.1" aria-hidden="true" class="github-icon" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.19 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg></a>');function Jr(e,t){let r=g(t,"link",8);var n=zr();U(()=>ue(n,"href",r())),m(e,n)}var Qr=w('<input type="search" class="input input-bordered w-64 text-base-content px-5">');function Xr(e,t){let r=g(t,"placeholder",8);var n=Qr();U(()=>ue(n,"placeholder",r())),m(e,n)}var Zr=w('<label class="flex flex-row cursor-pointer gap-2 px-5"><i class="material-icons text-primary-content">sunny</i> <input type="checkbox" class="toggle theme-controller"> <i class="material-icons text-primary-content">dark_mode</i></label>');function en(e,t){wt(t,!1);let r=g(t,"lightThemeName",8),n=g(t,"darkThemeName",8),i=Yt(!1);function l(){const s=K(i)?n():r();document.documentElement.setAttribute("data-theme",s),localStorage.setItem("theme",s)}qr(()=>{const s=localStorage.getItem("theme")||r();document.documentElement.setAttribute("data-theme",s),Ae(i,s===n())}),Br();var o=Zr(),a=N(E(o),2);Lr(a,()=>K(i),s=>Ae(i,s)),Tr("change",a,l),m(e,o),yt()}var tn=w('<div class="navbar-end"><!> <!> <!></div>');function rn(e,t){let r=g(t,"lightThemeName",8),n=g(t,"darkThemeName",8);var i=tn(),l=E(i);en(l,{get lightThemeName(){return r()},get darkThemeName(){return n()}});var o=N(l,2);Xr(o,{placeholder:"Search"});var a=N(o,2);Jr(a,{link:"https://github.com/rbrearton/py-htmx"}),m(e,i)}var nn=w('<div class="navbar-start"><div class="flex flex-row"><i class="material-icons text-primary-content px-5">school</i> <!></div></div>');function ln(e,t){let r=g(t,"title",8);var n=nn(),i=E(n),l=N(E(i),2);bt(l,{get title(){return r()},isPadded:!1}),m(e,n)}var on=w('<div class="navbar bg-primary text-primary-content shadow"><!> <!> <!></div>');function an(e,t){let r=g(t,"lightThemeName",8),n=g(t,"darkThemeName",8),i=g(t,"siteTitle",8);var l=on(),o=E(l);ln(o,{get title(){return i()}});var a=N(o,2);Kr(a);var s=N(a,2);rn(s,{get lightThemeName(){return r()},get darkThemeName(){return n()}}),m(e,l)}var sn=w('<div slot="drawerContent">This should go in the drawer side.</div>'),un=w('<div slot="drawerContent">The right menu</div>'),fn=w('<main slot="pageContent" class="p-10 flex flex-row justify-center">The main content</main>'),cn=w('<div slot="pageContent"><!></div>'),_n=w("<!> <!> <!>",1);function vn(e,t){let r=g(t,"siteTitle",8);g(t,"pageTitle",8);var n=_n(),i=et(n);an(i,{lightThemeName:"notes_light",darkThemeName:"notes_dark",get siteTitle(){return r()}});var l=N(i,2);He(l,{isRightDrawer:!1,$$slots:{drawerContent:(a,s)=>{var f=sn();m(a,f)},pageContent:(a,s)=>{var f=cn(),v=E(f);He(v,{isRightDrawer:!0,$$slots:{drawerContent:(u,_)=>{var p=un();m(u,p)},pageContent:(u,_)=>{var p=fn();m(u,p)}}}),m(a,f)}}});var o=N(l,2);Yr(o),m(e,n)}function dn(e){vn(e,{siteTitle:"Notes",pageTitle:"Home"})}Pr(dn,{target:document.getElementById("app")});