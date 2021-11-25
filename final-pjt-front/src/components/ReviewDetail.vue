<template>
  <b-container>
    <div class="bg-light">
      <div class="bg-light text-dark rounded mt-3">
        <br />
        <h1>Review</h1>
        <br />
        <div class="AddWrap">
          <form>
            <table class="tbAdd" width="100%">
              <colgroup>
                <col width="4%" />
                <col width="15%" />
              </colgroup>
              <tr>
                <th>Movie title</th>
                <td>{{ review["movie_title"] }}</td>
              </tr>
              <tr>
                <th>Title</th>
                <td>{{ review["title"] }}</td>
              </tr>
              <tr>
                <th>Writer</th>
                <td>{{ review["user"] }}</td>
              </tr>
              <tr>
                <th>User score</th>
                <td>{{ review["rank"] }}</td>
              </tr>
              <tr>
                <th>Content</th>
                <td class="txt_cont" v-html="content">{{ content }}</td>
              </tr>
              <tr>
                <th>Created_at</th>
                <td>
                  {{ review["created_at"].substr(0, 4) }}/{{
                    review["created_at"].substr(5, 2)
                  }}/{{ review["created_at"].substr(8, 2) }}.
                  {{ review["created_at"].substr(11, 5) }}
                </td>
              </tr>
              <tr>
                <th>Updated_at</th>
                <td>
                  {{ review["updated_at"].substr(0, 4) }}/{{
                    review["updated_at"].substr(5, 2)
                  }}/{{ review["updated_at"].substr(8, 2) }}.
                  {{ review["updated_at"].substr(11, 5) }}
                </td>
              </tr>
            </table>
          </form>
        </div>
        <!-- 작성자 본인일 경우만 수정, 삭제 버튼 표시 -->
        <span v-if="$store.state.user === review['user']">
          <b-button @click="to_update_review"> Modify </b-button>
        </span>
        <span v-if="this.$store.state.user === review['user']">
          <b-button @click="delete_review" class="mx-1"> Delete </b-button>
        </span>
        <span>
          <b-button @click="moveToReviews" class="my-2">List</b-button>
        </span>

        <div class="d-flex mx-2 mb-1" style="align-items: center">
          <b-icon
            icon="chat-left-dots"
            class="d-flex"
            style="display: flex; margin-left: 1rem; margin-right: 8px"
          ></b-icon>
          <span class="text-start">comment</span>
        </div>
        <textarea
          v-model="my_comment.content"
          type="text"
          required
          style="
            overflow: auto;
            width: 95%;
            height: 50px;
            word-break: break-all;
          "
          class="rounded"
        ></textarea>
        <b-button @click="make_comment" class="mb-2">Submit</b-button>
        <!-- 댓글이 있다면 표시 -->
        <span v-if="comments[0].data.length">
          <b-list-group v-for="comment in comments[0].data" :key="comment.id">
            <b-list-group-item variant="dark">
              <!-- 댓글 수정중이 아닐 경우 -->
              <div v-if="!(updating_comment_id === comment.id)">
                <div>
                  <div
                    class="row"
                    style="
                      width: 300px;
                      margin: 8px 8px 8px 0px;
                      text-align: left;
                    "
                  >
                    <div style="width: 100px">
                      <b>{{ comment.userName }}</b>
                    </div>
                  </div>
                  <div
                    style="
                      margin: 8px 8px 8px 16px;
                      text-align: left;
                      word-break: break-all;
                    "
                    class="justify-content-start"
                  >
                    {{ comment.content }}
                  </div>

                  <div
                    class="row"
                    style="
                      width: 1500px;
                      margin: 16px 8px 8px 0px;
                      text-align: left;
                    "
                  >
                    <div
                      style="
                        width: 155px;
                        color: #5c636a;
                        display: flex;
                        align-items: center;
                      "
                      class="col-2"
                    >
                      {{ comment.updated_at.substr(0, 4) }}/{{
                        comment.updated_at.substr(5, 2)
                      }}/{{ comment.updated_at.substr(8, 2) }}.
                      {{ comment.updated_at.substr(11, 5) }}
                    </div>
                    <!-- 댓글 작성자 본인이면 수정, 삭제 버튼 표시 -->
                    <div
                      v-if="$store.state.user === comment.userName"
                      class="col-2 jutify-content-start"
                    >
                      <div class="row justify-content-start">
                        <span class="col-4">
                          <b-button
                            @click="
                              to_update_comment(comment.content, comment.id)
                            "
                          >
                            Modify
                          </b-button>
                        </span>
                        <span class="col-4">
                          <b-button @click="delete_comment(comment.id)">
                            Delete
                          </b-button>
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- 댓글 수정중일 경우 그 댓글만 수정창으로 표시 -->
              <div v-if="updating_comment_id === comment.id">
                <textarea
                  v-model="updating_comment.content"
                  type="text"
                  required
                  style="
                    overflow: auto;
                    width: 95%;
                    height: 100px;
                    word-break: break-all;
                  "
                  class="rounded"
                ></textarea>
                <span v-if="$store.state.user === comment.userName">
                  <b-button
                    @click="updateComment(comment.id)"
                    class="my-2 mx-2"
                  >
                    Done
                  </b-button>
                  <b-button @click="cancelComment">Cancel</b-button>
                </span>
              </div>
            </b-list-group-item>
          </b-list-group>
        </span>
      </div>
    </div>
  </b-container>
</template>

<script>
import axios from "axios";

export default {
  name: "ReviewDetail",
  data() {
    return {
      review: {
        movie_title: "",
        title: "",
        content: "",
        rank: "",
        created_at: "",
        updated_at: "",
        user: "",
      },
      my_comment: {
        content: "",
      },
      comments: [],
      updating_comment_id: null,
      updating_comment: {
        content: "",
      },
    };
  },
  methods: {
    getReview: function () {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/community/${this.$store.state.detailnum}/`,
        headers: this.$store.getters.config,
      })
        .then((res) => {
          this.review.movie_title = res.data.movie_title;
          this.review.title = res.data.title;
          this.review.rank = res.data.rank;
          this.review.content = res.data.content;
          this.review.created_at = res.data.created_at;
          this.review.updated_at = res.data.updated_at;
          this.review.user = res.data.userName;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    make_comment: function () {
      if (this.my_comment.content) {
        if (this.my_comment.content.trim()) {
          axios({
            method: "post",
            url: `http://127.0.0.1:8000/community/${this.$store.state.detailnum}/comments/create/`,
            headers: this.$store.getters.config,
            data: this.my_comment,
          })
            .then(() => {
              this.my_comment.content = null;
              this.get_comments();
            })
            .catch((error) => {
              console.log(error);
            });
        } else {
          alert(`Please input content.`);
        }
      } else {
        alert(`Please input content.`);
      }
    },
    get_comments: function () {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/community/${this.$store.state.detailnum}/comments/`,
        headers: this.$store.getters.config,
      })
        .then((res) => {
          this.comments.unshift(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    delete_comment: function (comment_pk) {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/community/${comment_pk}/comments/delete/`,
        headers: this.$store.getters.config,
      })
        .then(() => {
          this.get_comments();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    delete_review: function () {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/community/${this.$store.state.detailnum}/`,
        headers: this.$store.getters.config,
      })
        .then(() => {
          alert("Completely deleted.");
          this.$router.push({ name: "Reviews" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    to_update_comment: function (cont, comment_pk) {
      this.updating_comment.content = cont;
      this.updating_comment_id = comment_pk;
    },
    cancelComment: function () {
      this.updating_comment_id = null;
    },
    to_update_review: function () {
      const data = {
        movie_title: this.review.movie_title,
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank,
        writer: this.review.user,
      };
      if (localStorage.getItem("jwt")) {
        this.$store.dispatch("toUpdateReview", data);
        this.$router.push({ name: "UpdateReview" });
      } else {
        this.$router.push({ name: "Login" });
      }
    },
    updateComment: function (comment_pk) {
      if (this.updating_comment.content.trim()) {
        axios({
          method: "put",
          url: `http://127.0.0.1:8000/community/${comment_pk}/comments/update/`,
          headers: this.$store.getters.config,
          data: this.updating_comment,
        })
          .then(() => {
            this.updating_comment_id = null;
            this.get_comments();
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        alert(`Please input content.`);
      }
    },
    moveToReviews: function () {
      this.$router.push({ name: "Reviews" });
    },
  },
  created: function () {
    if (this.$store.state.token) {
      this.getReview();
      this.get_comments();
      // 로그인하지 않은 유저면 로그인페이지로
    } else {
      this.$router.push({ name: "Login" });
    }
  },
  computed: {
    content() {
      return this.review.content.split("\n").join("<br>");
    },
  },
};
</script>

<style scoped>
.tbAdd {
  border-top: 1px solid #888;
}
.tbAdd th,
.tbAdd td {
  border-bottom: 1px solid #eee;
  padding: 5px 0;
}
.tbAdd td {
  padding: 10px 10px;
  box-sizing: border-box;
  text-align: left;
}
.tbAdd td.txt_cont {
  height: 300px;
  vertical-align: top;
}
</style>
