<template>
  <b-container class="movie-detail w-100 pt-3">
    <div
      class="movie-detail-image"
      :style="{ backgroundImage: `url(${background_poster})` }"
    ></div>
    <div class="movie-content d-flex">
      <div class="col-lg-5 col-md-5 col-sm-5 col-0">
        <div>
          <b-img
            class="px-1 py-2"
            :src="`https://image.tmdb.org/t/p/original${poster}`"
            fluid-grow
            alt="img"
          >
          </b-img>
        </div>
        <br />
        <div class="d-flex d-flex justify-content-center">
          <radial-progress-bar
            clss="col-6"
            :diameter="150"
            :innerStokewidth="60"
            :strokeWidth="15"
            stopColor="#FFC107"
            startColor="#FCDD7B"
            :completed-steps="originalRate"
            :total-steps="totalScore"
          >
            <div>
              <p class="fw-bold">
                User <br />
                Score
              </p>
              <p>{{ originalRate }} %</p>
            </div>
          </radial-progress-bar>
          <div class="fs-5 mx-3 fw-bolder lh-base">
            <label class="rating-box" for="rating-inline"> </label><br />
            <b-form-rating
              class="bg-transparent"
              id="rating-inline"
              v-model="currentRate"
              no-border
              inline
              variant="warning"
              @change="giveRate"
            >
            </b-form-rating>
            <br />
            <!-- 로그인한 사람이 평가한 경우만 표시 -->
            <div class="pt-1" v-if="currentRate && this.$store.state.token">
              My score : {{ currentRate }}
            </div>
            <div v-else>Rate it !</div>
          </div>
        </div>
      </div>
      <div class="px-3">
        <div>
          <h2 class="mx-3 py-3 fw-bolder lh-base">
            {{ title }} ({{ release_date.substr(0, 4) }})
          </h2>
        </div>
        <div class="fs-5 mx-3 my-3 me-5 lh-base text-start">
          <p class="fs-4 fw-bolder">overview :</p>
          {{ overview }}
        </div>
        <div>
          <p class="fs-5 mx-3 my-3 text-start">
            Genres :
            <span v-for="genre in this.genres" :key="genre.id">
              {{ genre.name }} &nbsp;
            </span>
          </p>
        </div>
        <div>
          <p class="fs-5 mx-3 my-3 text-start text-break">
            Director:
            <span v-for="director in this.directors" :key="director.id">
              {{ director.name }}
            </span>
          </p>
        </div>
        <div>
          <p class="fs-5 mx-3 my-3 lh-base text-break text-start">
            Cast :
            <span v-for="actor in this.actors" :key="actor.id">
              {{ actor.name }}.&nbsp;
            </span>
          </p>
        </div>
        <div class="fs-5 mx-3 my-3 lh-base text-start">
          <br />
          <p>Release date : {{ release_date }}</p>
          <p>Runtime : {{ runtime }} min.</p>
        </div>
        <div>
          <br />
          <b-button
            class="mx-auto"
            v-if="this.$store.state.token"
            @click="toCreateReview"
          >
            Create review
          </b-button>
        </div>
      </div>
    </div>
    <div class="movie-content">
      <div class="fs-2 fw-border mx-3 py-5 lh-base text-start">Trailer</div>
      <b-embed
        type="iframe"
        aspect="16by9"
        :src="`https://www.youtube.com/embed/${video.videoId}`"
        clas="pt-5"
        width="800"
        height="450"
        frameborder="100"
        allowfullscreen
      >
      </b-embed>
    </div>
  </b-container>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";
import RadialProgressBar from "vue-radial-progress";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;
const API_KEY = "AIzaSyBOLP6YlcHq6sFO7W4KdSJ8qzo8UpeYSKM";
const API_URL = "https://www.googleapis.com/youtube/v3/search";

export default {
  name: "MovieDetail",
  data: function () {
    return {
      originalRate: 0,
      currentRate: 0,
      key: this.$store.state.movieKey,
      title: "",
      overview: "",
      poster: "",
      video: "",
      actors: "",
      mainactors: "",
      directors: "",
      genres: "",
      release_date: "",
      runtime: "",
      background_poster: "",
      totalScore: 100,
      ratingDone: 0,
    };
  },
  components: {
    RadialProgressBar,
  },
  methods: {
    movieinfo: function () {
      axios({
        method: "get",
        url: `${SERVER_URL}/movies/${this.key}`,
      })
        .then((res) => {
          this.originalRate = res.data.vote_average * 10;
          this.title = res.data.title;
          this.overview = res.data.overview;
          this.poster = res.data.poster_path;
          this.actors = res.data.actors;
          this.directors = res.data.directors;
          this.genres = res.data.genres;
          this.release_date = res.data.release_date;
          this.runtime = res.data.runtime;
          this.mainactors = res.data.actors.slice(0, 5);
          this.background_poster =
            "https://image.tmdb.org/t/p/original" + res.data.backdrop_path;
          return this;
        })
        .then(function (res) {
          res.get_video();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_video: function () {
      const params = {
        key: API_KEY,
        part: "snippet",
        q: this.title,
        type: "video",
        maxResults: 1,
      };
      axios({
        method: "get",
        url: API_URL,
        params,
      })
        .then((res) => {
          this.video = res.data.items[0].id;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    giveRate: function () {
      // 로그인 상태라면
      if (this.$store.state.token) {
        const rate = this.currentRate;
        alert(`Thanks for your feedback : ${this.currentRate}.`);
        // 별점 이미 줬으면
        if (this.ratingDone > 0) {
          axios({
            method: "put",
            url: `${SERVER_URL}/movies/${this.$store.state.movieKey}/rates`,
            headers: this.$store.getters.config,
            data: {
              rate: rate,
            },
          }).catch((err) => {
            console.error(err);
          });
          // 별점을 주지 않았으면 post
        } else {
          axios({
            method: "post",
            url: `${SERVER_URL}/movies/${this.$store.state.movieKey}/rates`,
            headers: this.$store.getters.config,
            data: {
              rate: rate,
            },
          })
            .then(() => {
              this.ratingDone = 1;
            })
            .catch((err) => {
              console.error(err);
            });
        }
        // 로그인하지 않았다면
      } else {
        this.currentRate = 0;
        alert(`Please login`);
        location.reload();
      }
    },
    toCreateReview: function () {
      if (localStorage.getItem("jwt")) {
        this.$store.dispatch("yesTitle");
        this.$router.push({ name: "CreateReview" });
      } else {
        this.$router.push({ name: "Login" });
      }
    },
  },
  created: function () {
    this.movieinfo();
    axios({
      method: "get",
      url: `${SERVER_URL}/movies/${this.$store.state.movieKey}/rates`,
      headers: this.$store.getters.config,
    }).then((res) => {
      if (res.data.rate) {
        this.currentRate = res.data.rate;
        this.ratingDone = 1;
      }
    }),
      this.$store.dispatch("LoadMovieList");
  },
  computed: {
    ...mapState(["URL"]),
    ...mapState(["moviekey"]),
  },
};
</script>

<style>
.movie-detail {
  position: relative;
  padding: 40px 40px;
}

.movie-detail-image {
  background-size: cover;
  height: 80%;
  position: fixed;
  top: 10%;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.movie-detail-image::after {
  top: 10%;
  left: 0;
  right: 0;
  bottom: 0;
  min-height: 100vh;
  background-color: rgb(40, 40, 40);
  opacity: 0.8;
  content: "";
  z-index: 0;
  display: block;
}

.movie-content {
  position: relative;
  z-index: 10;
}
</style>
