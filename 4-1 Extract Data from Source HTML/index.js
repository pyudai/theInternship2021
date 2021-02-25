let axios = require('axios');
let cheerio = require('cheerio');
let URL = 'https://theinternship.io';

const getPicURL = async function(){
	const res = await axios.get(URL);
	const html = await res.data;
	const $ = cheerio.load(html);

	let pic = $('div.partner').map(function (i,el){
		return {'pic':$('div.partner >.logo-box > a > img').eq(i).attr('src'),'len':$(this).text().length};
	}).get().sort(function(a, b){return a.len - b.len}).map((p)=> p.pic);
	return pic;
}
;(async ()=>{
	let picURL=await getPicURL();
	picURL.map((p)=> console.log(p));
})();