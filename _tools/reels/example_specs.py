import json
S='stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"'
IC={
'globe':f'<svg width="46" height="46" viewBox="0 0 24 24" {S}><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
'cal':f'<svg width="46" height="46" viewBox="0 0 24 24" {S}><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
'vid':f'<svg width="46" height="46" viewBox="0 0 24 24" {S}><rect x="3" y="6" width="13" height="12" rx="3"/><path d="m16 10 5-3v10l-5-3"/></svg>',
'pay':f'<svg width="46" height="46" viewBox="0 0 24 24" {S}><rect x="3" y="6" width="18" height="13" rx="3"/><path d="M3 10h18M7 15h4"/></svg>',
'check':f'<svg width="46" height="46" viewBox="0 0 24 24" {S}><path d="m5 12 5 5 9-10"/></svg>',
}
def li(ic,t,d,ml=False): return f'<div class="li in" style="--d:{d}s"><span class="ic">{IC[ic]}</span><b class="{"ml" if ml else ""}">{t}</b></div>'

ml={"scenes":[
 {"dur":5,"html":'<div class="kick ml in">ഡോക്ടർമാർ ശ്രദ്ധിക്കൂ</div><h1 class="ml in" style="--d:.2s">രോഗികൾ ആദ്യം തിരയുന്നത് <span class="grad">Google-ലും Instagram-ലും</span></h1>'},
 {"dur":4,"html":'<h1 class="ml pop">നിങ്ങൾക്ക് സ്വന്തമായി ഒരു <span class="grad">ഓൺലൈൻ ക്ലിനിക്ക്</span> ഉണ്ടോ?</h1>'},
 {"dur":7,"html":'<div class="kick ml in">DotCom by Arshees ഒരുക്കുന്നു</div>'+li('globe','സ്വന്തം ഡൊമൈനിൽ വെബ്സൈറ്റ്',.3,True)+li('cal','ഓൺലൈൻ അപ്പോയിന്റ്മെന്റ് ബുക്കിംഗ്',1.4,True)},
 {"dur":7,"html":'<div class="kick ml in">ഒപ്പം</div>'+li('vid','വെബ്സൈറ്റിനുള്ളിൽ വീഡിയോ കൺസൾട്ടേഷൻ',.2,True)+li('pay','കോളിന് മുമ്പ് UPI വഴി ഫീസ്',1.6,True)},
 {"dur":6,"html":'<h2 class="ml in">നിങ്ങളുടെ <span class="grad">സൗജന്യ സാമ്പിൾ സൈറ്റ്</span> കാണൂ</h2><div class="pill pop" style="--d:.6s">arshees.com/portal</div><p class="lead in" style="--d:1s">Your own online clinic — free sample.</p>'},
]}
en={"scenes":[
 {"dur":4,"html":'<div class="kick in">For doctors</div><h1 class="in" style="--d:.2s">Before a patient books you, they check <span class="grad">3 things</span></h1>'},
 {"dur":4.5,"html":'<div class="big grad pop">1</div><h2 class="in" style="--d:.3s">Can I book online — <span class="grad">right now</span>, without calling?</h2>'},
 {"dur":4,"html":'<div class="big grad pop">2</div><h2 class="in" style="--d:.3s">Can I <span class="grad">consult by video</span> if I can\'t come in?</h2>'},
 {"dur":6,"html":'<div class="big grad pop">3</div><h2 class="in" style="--d:.3s">Does this doctor look <span class="grad">trustworthy?</span></h2><p class="lead in" style="--d:1.2s">Real photos · clear timings · a proper website</p>'},
 {"dur":8,"html":'<div class="kick in">DotCom by Arshees builds your online clinic</div>'+li('cal','Online booking',.4)+li('vid','Video consults inside your site',1.6)+li('pay','UPI fee before the call',3.0)},
 {"dur":5,"html":'<h2 class="in">See your <span class="grad">free sample</span></h2><div class="pill pop" style="--d:.5s">arshees.com/portal</div>'},
]}
json.dump(ml,open('ml.json','w'),ensure_ascii=False);json.dump(en,open('en.json','w'))
