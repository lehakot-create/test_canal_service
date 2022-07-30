import React, { Component } from "react";
import "./App.css";

const PLACES = [
  { name: "Palo Alto", zip: "94303" },
  { name: "San Jose", zip: "94088" },
  { name: "Santa Cruz", zip: "95062" },
  { name: "Honolulu", zip: "96803" }
];

class WeatherDisplay extends Component {
  constructor() {
    super();
    this.state = {
      weatherData: null
    };
  }
  componentDidMount() {
    const URL = "http://127.0.0.1:8000/api/v1/orders/";
    fetch(URL).then(res => res.json()).then(json => {
      this.setState({ Data: json });
    });
  }
  render() {
    const Data  = this.state;

    return (
        // {Data.map(({ id, order })) => (
        //     <div>
        //         <span>{id}</span>
        //         <span>{order}</span>
        //     </div>
        // )}
        JSON.parse(Data, function (key, value){
        console.log(key))
  }

class App extends Component {
  constructor() {
    super();
    this.state = {
      activePlace: 0
    };
  }
  render() {
    const activePlace = this.state.activePlace;
    return (
      <div className="App">
        {PLACES.map((place, index) => (
          <button
            key={index}
            onClick={() => {
              this.setState({ activePlace: index });
            }}
          >
            {place.name}
          </button>
        ))}
        <WeatherDisplay key={activePlace} zip={PLACES[activePlace].zip} />
      </div>
    );
  }
}

export default App;