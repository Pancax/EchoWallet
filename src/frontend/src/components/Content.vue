<template>
  <main class="col-md-9 ml-sm-auto col-lg-10">
    <div class="charts" v-for="(chart, index) in charts" :key="index">
      <ChartContainer :chart="chart" v-if="chart.chart_name === active_chart" />
    </div>
  </main>
</template>

<script>
import ChartContainer from './ChartContainer.vue';
export default {
  components: {
    ChartContainer,
  },
  props: ['active_chart', 'charts'],
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
