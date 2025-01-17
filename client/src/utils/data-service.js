import Vue from 'vue';

let DataService = new Vue({
  data:{
    // This url should align with backend
    dataServerUrl: 'http://127.0.0.1:5000',
  },

  methods:{
    // HTTP GET request
    loadGet(callback){
      this.axios.get(`${this.dataServerUrl}/get`)
        .then(response => {
          callback(response.data)
        }, errResponse => {
          console.log(errResponse)
        })
    },
    // load mapdata
    loadMapData(callback){
      this.axios.get(`${this.dataServerUrl}/getdata`)
        .then(response => {
          callback(response.data)
        }, errResponse => {
          console.log(errResponse)
        })
    },


    // HTTP POST request
    loadPost(param, callback){
      this.axios.post(`${this.dataServerUrl}/post`, param)
        .then(response => {
          callback(response.data)
        }, errResponse => {
          console.log(errResponse)
        })
    },

    //loadMapDataBy parameter
    // loadMapParameterData(param, callback){
    //   this.axios.post(`${this.dataServerUrl}/get_data_by_param`,param)
    //     .then(response => {
    //       callback(response.data)
    //     }, errResponse => {
    //       console.log(errResponse)
    //     })
    // },
  }
});

export default DataService;
