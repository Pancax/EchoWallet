<template>
  <main class="col-md-9 ml-sm-auto col-lg-10">
    <div v-for="(prediction, index) in predicts" :key="index">
      <div class="row" v-if="prediction.name === active_chart">
        <div class="col">
          <h4>
            Our algorithim determined that this stock's value is highly
            correlated with our social media metrics. So we recommend buying it.
          </h4>
        </div>
        <div class="col">
          <h4>R Value: {{ prediction.r_value }}</h4>
        </div>
      </div>
    </div>

    <div v-for="(chart, index) in charts" :key="index">
      <div class="row" v-if="chart.chart_name === active_chart">
        <ChartContainer
          class="col"
          :chart="chart"
          style="width: 100%; height: auto"
        />
        <div class="container col">
          <img
            :src="
              'http://localhost:8080/api/messages/' + chart.chart_name + '.png'
            "
            alt=""
            style="width: 100%; height: auto"
          />
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import ChartContainer from './ChartContainer.vue';
export default {
  components: {
    ChartContainer,
  },
  props: ['active_chart', 'charts', 'predicts'],
  data() {
    return {
      hidden: false,
    };
  },
};
</script>

<style>
main {
  height: 100vh;
}
</style>
