<template>
  <b-container class="searchbar">
    <b-row>
      <!-- 서치바 왼쪽 춤추는 도지(중요!) -->
      <img
        src="../assets/doge.gif"
        alt="doge"
        style="display: inline-block; width: 6rem; height: 4rem"
      />
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
        class="col-2 fs-3 fw-bold text-md-center mx-2"
        @click="SearchMovie"
        ><b-icon icon="search"></b-icon> Search
      </b-button>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "MovieSearchbar",
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
      } else {
        this.$emit("search-movie", this.inputData);
      }
    },
  },
};
</script>

<style>
.searchbar {
  padding: 2rem;
}
</style>
