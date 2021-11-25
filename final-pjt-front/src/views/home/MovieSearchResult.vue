<template>
  <b-container class="mh-100 mw-100">
    <div>
      <br />
      <h2>Search result</h2>
      <!-- 검색결과 있을 경우 -->
      <div
        class="d-flex flex-wrap justify-content-left"
        v-if="searchResults.length > 0"
      >
        <div
          class="py-3 px-2"
          v-for="result in searchResults"
          :key="result.id"
          @click="moveToDetail(result)"
        >
          <div style="width: 305px; height: 550px">
            <div>
              <img
                :src="`https://image.tmdb.org/t/p/w300${result.poster_path}`"
                alt="img"
                @click="moveToDetail(result)"
                style="width: 300; height: 450px; object-fit: contain"
                class="scale"
              />
            </div>
            <div class="px-2 py-2 fs-3 con" style="height: 100px">
              <div v-if="result.title.length > 24" class="overflow fs-4">
                {{ result.title }}
              </div>
              <div v-else class="fs-4">
                {{ result.title }}
              </div>
              <div class="fs-5">
                {{ result.release_date.substr(0, 4) }}
                <b>ㆍ</b> {{ result.genres[0].name }}
              </div>
            </div>
          </div>
        </div>
        <br />
      </div>
      <!-- 검색결과 없을 경우 -->
      <div v-else>
        <br />
        <br />
        <div>
          <div><b-icon icon="spellcheck" class="h1 mb-2"></b-icon></div>
          <br />
          <div>
            <h4>There are no movies that matched your query.</h4>
            <h4>Please check spelling.</h4>
          </div>
        </div>
      </div>
    </div>
  </b-container>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "MovieSearchResult",
  methods: {
    moveToDetail: function (data) {
      this.$store.dispatch("GetId", data);
      this.$router.push({ name: "MovieDetail" });
    },
  },
  computed: {
    ...mapGetters(["searchResults"]),
  },
};
</script>

<style>
.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;
}
.scale:hover {
  transform: scale(1.1);
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
}
.img {
  overflow: hidden;
}

.overflow {
  height: 70px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  align-items: center;
}
</style>
