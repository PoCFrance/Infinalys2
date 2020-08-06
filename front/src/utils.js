import { tsvParse} from "d3-dsv";
import { timeParse } from "d3-time-format";

var parseDate = timeParse("%Y-%m-%d");

function parseData(parse) {
	return function(d) {
		d.date = parseDate(d.Date);
		// var curentday = new Date()
		// if (curentday < d.date) {
		// 	console.log(curentday)
		// 	console.log(d.date)
		// }
		d.open = +d.Open;
		d.high = +d.High;
		d.low = +d.Low;
		d.close = +d.Close;
		d.volume = +d.Volume;
		return d;
	};
}


//https://cdn.rawgit.com/rrag/react-stockcharts/master/docs/data/MSFT.tsv 
//http://0.0.0.0:5000/?stock=AAPL&interval=3mo

export function getData(value) {
	var str = "http://localhost:5000/?stock=AAPL&interval=1d"

	if (value === "TEST") {
		str = "https://cdn.rawgit.com/rrag/react-stockcharts/master/docs/data/MSFT.tsv"
	}
	if (value === "TESLA") {
		str = "http://0.0.0.0:5000/?stock=TESLA&interval=1mo"
	}
	if (value === "APPL") {
		str = "http://localhost:5000/?stock=AAPL&interval=1mo"
	}
	const promiseMSFT = fetch(str)
		.then(response => response.text())
		.then(data => tsvParse(data, parseData(parseDate)))
	return promiseMSFT;
}
