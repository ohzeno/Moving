<template>
  <b-container>
    <div>
      <div>
        <h1 class="my-3">Update review</h1>
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
              <div>Title</div>
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
              <div style="text-align: center">User score</div>
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
          <b-button @click="moveToReviews" class="my-3">List</b-button>
        </span>
        <span>
          <b-button @click="updateReview" class="mx-1">Complete</b-button>
        </span>
        <span>
          <b-button @click="toDetail" class="my-3">Cancel</b-button>
        </span>
      </div>
    </div>
  </b-container>
</template>

<script>
import axios from "axios";

export default {
  name: "ReviewUpdate",
  data() {
    return {
      review: {
        movie_title: "",
        title: "",
        content: "",
        rank: "",
      },
      writer: "",
    };
  },
  methods: {
    updateReview: function () {
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
            method: "put",
            url: `http://127.0.0.1:8000/community/${this.$store.state.detailnum}/`,
            headers: this.$store.getters.config,
            data: {
              movie_title: this.review.movie_title,
              title: this.review.title,
              content: this.review.content,
              rank: this.review.rank,
            },
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
    getContent: function () {
      this.review.movie_title = this.$store.state.updateReview.movie_title;
      this.review.title = this.$store.state.updateReview.title;
      this.review.content = this.$store.state.updateReview.content;
      this.review.rank = this.$store.state.updateReview.rank;
    },
    toDetail: function () {
      this.$router.push({ name: "ReviewDetail" });
    },
    moveToReviews: function () {
      this.$router.push({ name: "Reviews" });
    },
  },
  created: function () {
    if (this.$store.state.token) {
      // 로그인했고, 작성자 본인이라면
      if (this.$store.state.user === this.$store.state.updateReview.writer) {
        this.getContent();
        this.writer = this.$store.state.updateReview.writer;
        // 로그인했지만 작성자 본인이 아니면 디테일페이지로
      } else {
        this.$router.go(-1);
      }
      // 로그인하지 않은 유저면 로그인페이지로
    } else {
      this.$router.push({ name: "Login" });
    }
  },
};
</script>

<style></style>
