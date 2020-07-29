import React from 'react';
import Chart from './Chart_candle';
import { getData } from "./utils"
import { TypeChooser } from "react-stockcharts/lib/helper";
import Checkbox from '@material-ui/core/Checkbox';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
// import ButtonAppBar from './AppBar'


import useMediaQuery from '@material-ui/core/useMediaQuery';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';

//MARK: this way is for chart component
class ChartComponent extends React.Component {
	componentDidMount() {
		getData().then(data => {
			this.setState({ data })
		})
	}
	render() {
		if (this.state == null) {
			return <div>Loading...</div>
		}
		return (
			<TypeChooser>
				{type => <Chart type={type} data={this.state.data} Boolez={this.props.boolinger}/>}
			</TypeChooser>
		)
	}
}



function App() {
  const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');

  const theme = React.useMemo(
    () =>
      createMuiTheme({
        palette: {
          type: prefersDarkMode ? 'dark' : 'light',
        },
      }),
    [prefersDarkMode],
  );

  const [state, setState] = React.useState({
    Boll: false,
  });

  const handleChange = (event) => {
    setState({ ...state, [event.target.name]: event.target.checked });
  };


  return(
    <div>
      <ThemeProvider theme={theme}>
        <CssBaseline/>
        <ChartComponent boolinger={state.Boll}/>
        <FormControlLabel
          control = {
            <Checkbox
              checked = {state.Boll}
              onChange = {handleChange}
              name = 'Boll'
              color = 'primary'
            />
          }
          label = "Boll"
        />
        <FormControl>
          <InputLabel>Boursse</InputLabel>
          <Select
            native
            value={state.age}
            //onChange={handleChange}
            inputProps={{
              name: 'Boursse',
            }}
          >
          <option aria-label="None" value="" />
          <option value={() => console.log("TESLA")}>TESLA</option>
          <option value={() => console.log("APPL")}>APPL</option>
          <option value={() => console.log("BTC")}>BTC-USD</option>
          </Select>
        </FormControl>
      </ThemeProvider>
    </div>
  );
}

export default App;
