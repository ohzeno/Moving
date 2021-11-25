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
      if (this.inputData) {
        //글자 존재하고 공백 아님
        if (this.inputData.trim()) {
          // 공백 제거 후에 2글자 미만임
          if (this.inputData.trim().length < 2) {
            alert("Please type at least two letters.");
            // 공백 제거해도 2글자 이상이면 진행
          } else {
            // 검색 후 검색창 입력값 초기화
            const inputD = this.inputData;
            this.inputData = null;
            this.$emit("search-movie", inputD);
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

<style></style>
