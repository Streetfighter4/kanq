import {Component, Input, OnInit} from '@angular/core';
import {CommentService} from './comment.service';
import {Comment} from './comment';

@Component({
  selector: 'comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.css']
})
export class CommentComponent implements OnInit {
  @Input() comment: Comment;

  showReplyBox: boolean = false;
  replyText: string;

  constructor(private commentService: CommentService) { }

  ngOnInit() {
  }

  openReplyBox() {
    this.showReplyBox = true;
  }

  createChildComment() {
    this.commentService.createComment(this.replyText, this.comment, this.comment.post)
      .then(this.handleCommentCreation.bind(this));
  }

  handleCommentCreation(newComment: Comment) {
    this.resetReplyBox();
    this.comment.children.push(newComment);
  }

  resetReplyBox() {
    this.showReplyBox = false;
    this.replyText = '';
  }
}
