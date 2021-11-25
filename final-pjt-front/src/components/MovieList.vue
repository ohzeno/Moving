<template>
  <div>
    <div style="width: 305px; height: 550px">
      <div class="px-2 py-2 fs-3 con" style="height: 100px">
        <div v-if="movie.title.length > 24" class="overflow">
          {{ movie.title }}
        </div>
        <div v-else>
          {{ movie.title }}
        </div>
      </div>
      <div>
        <img
          :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`"
          @click="moveToDetail(movie)"
          alt="test"
          style="width: 300; height: 450px; object-fit: contain"
          class="scale"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieList",
  props: {
    movie: Object,
  },
  methods: {
    moveToDetail: function (data) {
      this.$store.dispatch("GetId", data);
      this.$router.push({ name: "MovieDetail" });
    },
  },
};
</script>

<style scoped>
.con {
  display: flex;
  justify-content: center;
  align-items: center;
}
.overflow {
  height: 85px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  align-items: center;
}
</style>
