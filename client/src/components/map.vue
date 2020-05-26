
<template>
    <div>
        <el-row>
            <el-select v-model="country_value" placeholder="请选择">
                <el-option
                  v-for="item in country_options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                >
                </el-option>
             </el-select>
            <el-select v-model="AQS_value" placeholder="请选择">
                <el-option
                  v-for="item in AQS_options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                >
                </el-option>
             </el-select>
        </el-row>

        <div id="map"></div>
    </div>
</template>

<script>
    /*
      This component demonstrates one way to construct leaflet map. (https://leafletjs.com/reference-1.6.0.html#map-example)
    */

    import * as L from "leaflet";
    // import DataService from "./utils/data-service";
    // import EventService from "./utils/event-service";


    export default {
        name: "Map",
        props: {
          mapData: Object,
        },
        data() {
          return {
            country_options: [{
              value: 'CN',
              label: 'China'
            }, {
              value: 'US',
              label: 'America'
            }],
            country_value: '',
            AQS_options: [
                {
                  value: 'co',
                  label: 'CO'
                },
                {
                  value: 'pm25',
                  label: 'pm2.5'
                },
                {
                  value: 'pm10',
                  label: 'pm1.0'
                },
                {
                  value: 'so2',
                  label: 'SO2'
                },
                {
                  value: 'co2',
                  label: 'CO2'
                },
                {
                  value: 'o3',
                  label: 'O3'
                }],
            AQS_value: '',
          }
        },
        watch: {
          mapData: function () {
            // When data is changed in parent, render this component
            this.renderMap();
          },
          AQS_value:function () {

             this.map.removeLayer(this.layerGroup);
             this.renderMap();
          }

        },
        mounted: function () {
          this.initMap();
        },
        methods: {
            initMap(){
                // Initialize map figure
                // let width = this.$el.clientWidth;
                // let height = this.$el.clientHeight;

                //set the color

                this.cfg= {
                    color: ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462'],
                    type : ['co','pm25','pm10','so2','co2','o3']
                }

                var mapboxAccessToken ='pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw'

                this.map = L.map('map').setView([40.01,116.333],4)

                L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=' + mapboxAccessToken, {
                    id: 'mapbox/light-v9',
                    // attribution: ...,
                    tileSize: 512,
                    zoomOffset: -1
                }).addTo(this.map);

                this.renderMap();
            },
            renderMap(){
                // // draw area (dropped because of lack of boundary data)
                // let AQS_feature = AQS_data.map(d=>{
                //     let n = {}
                //     n.type = "Feature"
                //     n.geometry = {
                //         "type":"Point",
                //         "coordinates":[d.coordinates.latitude,d.coordinates.longitude]
                //     }
                //     n.properties = {
                //         "pm25":d.value
                //         // "date":d.date,
                //         // "parameter":d.parameter,
                //         // "value":d.value,
                //         // "unit":d.unit,
                //         // "averagingPeriod":d.averagingPeriod,
                //         // "country":d.country,
                //         // "city":d.city,
                //         // "location":d.location,
                //         // "attribution":d.attribution
                //     }
                //     return n
                // })
                // let geoAQSdata = {
                //     "type": "FeatureCollection",
                //     "features": AQS_feature
                // }
                // L.geoJson(geoAQSdata).addTo(this.map);
                console.log(this.mapData)


                let data = this.AQS_value ? this.mapData.filter(d=>d.parameter == this.AQS_value):this.mapData

                let layer =[]



                for(let index in data){
                    let point = data[index]
                     let circle = L.circle(point['coordinates'], {
                        color: this.cfg.color[this.cfg.type.indexOf(point['parameter'])],
                        weight: 2,
                        fillColor: this.cfg.color[this.cfg.type.indexOf(point['parameter'])],
                        fillOpacity: 0.5,
                        radius: 5000
                    })
                    layer.push(circle)
                    circle.bindPopup("Country: " + point['country'] + "<br/>" + 'City: ' + point['city'] + "<br/>")
                }
                this.layerGroup=L.layerGroup(layer);
                this.map.addLayer(this.layerGroup);


            }
        }
    }

</script>
<style scoped>
    #map{
        width:100%;
        height:90%
    }
    button{
        float:left;
    }
</style>