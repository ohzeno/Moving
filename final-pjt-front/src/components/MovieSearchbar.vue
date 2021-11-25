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
      // 글자 존재
      if (this.inputData) {
        //글자 존재하고 공백 아님
        if (this.inputData.trim()) {
          // 공백 제거 후에 2글자 미만임
          if (this.inputData.trim().length < 2) {
            alert("Please type at least two letters.");
            // 공백 제거해도 2글자 이상이면 진행
          } else {
            this.$emit("search-movie", this.inputData);
          }
          // 공백 제거 후에 글자 존재 안함= 완전 공백임
        } else {
          alert("There is an empty box.");
        }
        // 글자가 존재안함
      } else {
        alert("There is an empty box.");
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
