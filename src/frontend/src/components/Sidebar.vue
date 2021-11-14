<template>
  <nav
    class="col-md-2 d-none d-md-block sidebar seperator-right position-fixed"
    style="min-height: 100vh"
  >
    <div class="sidebar-sticky">
      <ul class="nav flex-column">
        <li
          class="nav-item option"
          v-for="(chart, index) in charts"
          :key="index"
        >
          <div @click="updateActiveChart(chart.chart_name)" class="nav-link">
            {{ chart.chart_name }}
          </div>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  props: ['charts'],
  methods: {
    updateActiveChart(chartName) {
      this.$emit('new_active_chart', chartName);
    },
  },
};
</script>

<style scoped>
.nav-link {
  color: white !important;
  font-size: 20px !important;
}
.nav-link:hover {
  color: white !important;
}
.option {
}
.option:hover {
  cursor: pointer;
  border-bottom: 2px solid blueviolet;
}
.seperator-right {
  border-right: 2px solid blueviolet;
}
</style>
