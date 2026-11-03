import fs from 'fs';
const src=fs.readFileSync('tools/index.src.html','utf8');
const st=fs.readFileSync('tools/states.json','utf8');
const d=JSON.stringify(JSON.parse(fs.readFileSync('data.json','utf8')));
fs.writeFileSync('index.html',src.replace('__STATES__',()=>st).replace('__DATA__',()=>d));
