<template>
  <div class="container">
    <v-chart class="chart" :option="option" />
  </div>
</template>

<script>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { CandlestickChart } from 'echarts/charts';
import { TitleComponent } from 'echarts/components';
import VChart from 'vue-echarts';
import { defineComponent } from 'vue';

use([CanvasRenderer, CandlestickChart, TitleComponent]);

export default defineComponent({
  name: 'HelloWorld',
  components: {
    VChart,
  },
  props: ['chart'],
  data() {
    return {
      option: {},
    };
  },
  mounted() {
    let chart_data = this.chart;
    this.createChart(chart_data);
  },
  methods: {
    createChart(chart_data) {
      //Create chart series data
      let series = [];
      for (let x = 0; x < chart_data.High.length; x++) {
        series.push([
          chart_data.Open[x],
          chart_data.Close[x],
          chart_data.Low[x],
          chart_data.High[x],
        ]);
      }

      this.option = {
        title: {
          text: chart_data.chart_name,
          textStyle: {
            fontSize: 32,
            color: 'white',
            fontWeight: 'lighter',
          },
          left: 50,
        },
        xAxis: {
          data: chart_data.Date,
        },
        yAxis: {},
        series: [
          {
            type: 'candlestick',
            data: series,
          },
        ],
      };
    },
  },
});
</script>

<style scoped>
.container {
  margin-top: 100px;
}
.chart {
  height: 70vh;
  width: 100vh;
}
</style>
