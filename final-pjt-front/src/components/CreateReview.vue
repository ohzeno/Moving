<template>
  <b-container>
    <div>
      <h1 class="my-3">Create review</h1>
      <b-form>
        <b-row>
          <b-col
            sm="2"
            style="display: flex; align-items: center"
            class="justify-content-center"
          >
            <div>Movie title</div>
          </b-col>
          <b-col>
            <b-form-group>
              <b-form-input
                v-model="review.movie_title"
                type="text"
                required
                autofocus
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <br />
        <b-row>
          <b-col
            sm="2"
            style="display: flex; align-items: center"
            class="justify-content-center"
          >
            <div>Review title</div>
          </b-col>
          <b-col>
            <b-form-group>
              <b-form-input v-model="review.title" required></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <br />
        <b-row>
          <b-col
            sm="2"
            style="display: flex; align-items: center"
            class="justify-content-center"
          >
            <div>Rated</div>
          </b-col>
          <b-col>
            <b-form-group>
              <b-form-input
                v-model="review.rank"
                type="number"
                min="0"
                max="5"
                required
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <br />
        <b-form-group>
          <b-form-textarea
            v-model="review.content"
            rows="10"
            required
            type="textarea"
          ></b-form-textarea>
        </b-form-group>
      </b-form>
      <span>
        <b-button @click="createReview" class="mx-1 my-3">Complete</b-button>
      </span>
      <span>
        <b-button @click="cancelReview" class="mx-1 my-3">Cancel</b-button>
      </span>
    </div>
  </b-container>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  data() {
    return {
      review: {
        movie_title: "",
        title: "",
        content: "",
        rank: null,
      },
    };
  },
  methods: {
    createReview: function () {
      if (
        this.review.movie_title &&
        this.review.title &&
        this.review.content &&
        this.review.rank
      ) {
        if (
          this.review.movie_title.trim() &&
          this.review.title.trim() &&
          this.review.content.trim()
        ) {
          axios({
            method: "post",
            url: "http://127.0.0.1:8000/community/create/",
            headers: this.$store.getters.config,
            data: this.review,
          })
            .then((res) => {
              this.$store.dispatch("toDetail", res.data.id);
              this.$router.push({ name: "ReviewDetail" });
            })
            .catch((err) => {
              console.log(err);
              alert("Please check Movie title");
            });
        } else {
          alert(`There's an empty box`);
        }
      } else {
        alert(`There's an empty box`);
      }
    },
    cancelReview: function () {
      this.$router.go(-1);
    },
    movieinfo: function () {
      axios({
        method: "get",
        url: `${SERVER_URL}/movies/${this.$store.state.movieKey}`,
      })
        .then((res) => {
          this.review.movie_title = res.data.title;
        })
        .then(function () {})
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    // 로그인 했다면
    if (this.$store.state.token) {
      // 디테일페이지에서 들어온거면 영화제목 가져오기
      if (!this.$store.state.notitle) {
        this.movieinfo();
      }
      // 로그인하지 않았다면 로그인 페이지로
    } else {
      this.$router.push({ name: "Login" });
    }
  },
};
</script>

<style></style>
