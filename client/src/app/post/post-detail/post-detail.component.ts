import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {PostService} from '../post.service';
import {Post} from '../post';
import {CommentService} from '../../comment/comment.service';

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit {
  id: number;
  post: Post;
  postVoted: boolean = false;

  showReplyBox: boolean = false;
  replyText: string;

  constructor(private route: ActivatedRoute,
              private postService: PostService,
              private commentService: CommentService) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.id = +params['id'];

      this.postService.getDetail(this.id)
        .then(res => this.post = res);
    });
  }

  rate(value: number) {
    this.postVoted = true;
    this.postService.rate(this.id, value);
  }

  openReplyBox() {
    this.showReplyBox = true;
  }

  createChildComment() {
    this.commentService.createComment(this.replyText, null, this.post.id)
      .then(this.handleCommentCreation.bind(this));
  }

  handleCommentCreation(newComment: Comment) {
    this.resetReplyBox();
    this.post.comments.push(newComment);
  }

  resetReplyBox() {
    this.showReplyBox = false;
    this.replyText = '';
  }
}
