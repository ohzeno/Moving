<template>
  <div class="small searchbar py-3">
    <div class="d-flex">
      <b-form-input
        size="lg"
        class="col text-secondary"
        v-model="inputData"
        @keyup.enter="SearchMovie"
        placeholder="Search for a movie..."
      >
      </b-form-input>
      <b-button
        variant="warning"
        class="fw-bold text-md-center mx-2"
        @click="SearchMovie"
        ><b-icon icon="search"></b-icon
      ></b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SmallSearchbar",
  data: function () {
    return {
      inputData: null,
    };
  },
  methods: {
    SearchMovie() {
      // 한글자 검색 제한
      if (this.inputData.length < 2) {
        alert("Please type at least two letters.");
        // 검색 후 검색창 입력값 초기화
      } else {
        const inputD = this.inputData;
        this.inputData = null;
        this.$emit("search-movie", inputD);
      }
    },
  },
};
</script>

<style></style>
