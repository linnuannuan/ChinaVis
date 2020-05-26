<template>
  <div id="app">
    <Map class="overview" :map-data="mapData"></Map>
  </div>
</template>

<script>
  import DataService from "./utils/data-service";
  import EventService from "./utils/event-service";
  // import EchartsBar from "./components/echarts-bar";
  // import D3Bar from "./components/d3-bar";
  import Map from "./components/map";

  export default {
    name: 'App',
    components: {
      // D3Bar,
      // EchartsBar,
      Map,
    },
    data() {
      return {
        // data for HTTP requests in DataService
        getData: null,
        loadParam: {'data': 'load'},
        loadData: null,
        mapData:null,

        // data for event handling in EventService
        dataName: null,
        dataValue: null
      }
    },
    mounted () {
      // HTTP GET request
      DataService.loadGet((data) => {
        this.getData = data;
      });

      // HTTP POST request
      DataService.loadPost(this.loadParam, (data) => {
        this.loadData = data;
      });

      //load map data
      DataService.loadMapData( (data)=>{
        this.mapData = data;
        // this.loadingMap = false;
      });

      // DataService.loadMapParameterData((data)=>{
      //   this.mapData = data;
      //   // this.loadingMap = false;
      // });


      // Event handling for d3-bar
      EventService.onSelected((name, value) => {
        this.dataName = name;
        this.dataValue = value;
      });
    }
  }
</script>

<style>

  #app {
    font-family: Roboto, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  .overview{
    position:absolute;
    left: 3%;
    width: 94%;
    height: 400px;
    border: 2px solid steelblue;
    border-radius: 4px;
  }
</style>
