<template>
  <div>
  <main-header/>
  <test-quetions/>
  </div>
</template>

<script>
import MainHeader from "@/components/MainHeader";
import TestQuetions from "@/components/TestQuetions";

export default {
  components: {TestQuetions, MainHeader}
}
</script>