<template>
  <body class="bg-light">
    <main-header/>
    <tests-list
        :tests="tests"
        :sessions="sessions"
    />
  </body>
</template>

<script>
import MainHeader from "@/components/MainHeader";
import TestsList from "@/components/TestsList";

export default {
  components: {TestsList, MainHeader},
  data() {
    return {
      tests: [],
      sessions: []
    }
  },
  created() {
    this.$load(async () => {
      this.tests = (await this.$api.tests.getAll()).data.results
    })
    this.$load(async () => {
      // id текущего пользователя
      this.sessions = (await this.$api.sessions.getAll(1)).data.results
    })
  }
}
</script>