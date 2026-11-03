import {geoPath} from 'd3-geo';
import {feature, mesh} from 'topojson-client';
import fs from 'fs';
const us = JSON.parse(fs.readFileSync('node_modules/us-atlas/states-albers-10m.json'));
const ab={"01":"AL","02":"AK","04":"AZ","05":"AR","06":"CA","08":"CO","09":"CT","10":"DE","11":"DC","12":"FL","13":"GA","15":"HI","16":"ID","17":"IL","18":"IN","19":"IA","20":"KS","21":"KY","22":"LA","23":"ME","24":"MD","25":"MA","26":"MI","27":"MN","28":"MS","29":"MO","30":"MT","31":"NE","32":"NV","33":"NH","34":"NJ","35":"NM","36":"NY","37":"NC","38":"ND","39":"OH","40":"OK","41":"OR","42":"PA","44":"RI","45":"SC","46":"SD","47":"TN","48":"TX","49":"UT","50":"VT","51":"VA","53":"WA","54":"WV","55":"WI","56":"WY"};
const p=geoPath().digits(1);
const out={};
for(const f of feature(us,us.objects.states).features){const a=ab[f.id]; if(!a) continue; const c=p.centroid(f); out[a]={n:f.properties.name,d:p(f),c:c.map(v=>Math.round(v))};}
fs.writeFileSync('/home/claude/states.json',JSON.stringify(out));
console.log(Object.keys(out).length, fs.statSync('/home/claude/states.json').size);
