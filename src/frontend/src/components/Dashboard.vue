<template>
  <div>
    <DashNav />
    <div class="container-fluid">
      <div class="row">
        <Sidebar @new_active_chart="updateActiveChart" :charts="charts" />
        <Content :active_chart="active_chart" :charts="charts" />
      </div>
    </div>
  </div>
</template>

<script>
import DashNav from './DashNav.vue';
import Sidebar from './Sidebar.vue';
import Content from './Content.vue';

export default {
  components: {
    DashNav,
    Sidebar,
    Content,
  },
  data() {
    return {
      charts: [],
      active_chart: '',
    };
  },
  methods: {
    updateActiveChart(chartName) {
      this.active_chart = chartName;
    },
  },
  mounted() {
    fetch('/api/messages/getStockCharts')
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        this.charts = data;
      });
  },
};
</script>

<style></style>
