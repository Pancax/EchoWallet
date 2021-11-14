<template>
  <div>
    <DashNav />
    <div class="container-fluid">
      <div class="btn-container seperator-btm">
        <div class="buttons-row row">
          <div class="col"><h4>Our Picks</h4></div>
        </div>
        <h3 style="position: fixed; left: 47%; top: 120px">
          {{ active_chart }}
        </h3>
      </div>
      <div class="row">
        <Sidebar @new_active_chart="updateActiveChart" :charts="charts" />
        <Content
          :active_chart="active_chart"
          :charts="charts"
          :predicts="predictions"
        />
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
      predictions: [],
      active_chart: '',
      isPortfolio: false,
    };
  },
  methods: {
    updateActiveChart(chartName) {
      this.active_chart = chartName;
    },
  },
  updated() {
    for (let x = 0; x < this.charts.length; x++) {
      this.predictions.forEach((a) => {
        if (a.name == this.charts[x].chart_name) {
          this.charts[x].r_value = a.r_value;
        }
      });
    }
    this.charts.sort((a, b) => parseFloat(b.r_value) - parseFloat(a.r_value));
  },
  mounted() {
    if (!this.isPortfolio) {
      fetch('/api/messages/getStockCharts')
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          this.charts = data;
        });
      fetch('/api/messages/getPredictions')
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          this.predictions = data;
        });
    }
  },
};
</script>

<style scoped>
.echo-btn {
  color: blueviolet !important;
  border-color: blueviolet !important;
}
.echo-btn:hover {
  background-color: blueviolet;
  color: white !important;
  transition-duration: 0.5s;
}
.seperator-btm {
  padding-top: 20px;
  border-bottom: 2px solid blueviolet;
  margin-bottom: 5px;
}
.buttons-row {
  margin-bottom: 20px;
}
.btn-container {
  width: 100% !important;
  margin: 5px;
}
</style>
