import {Component, Input, OnInit} from '@angular/core';
import {CommentService} from '../comment/comment.service';

@Component({
  selector: 'reply-box',
  templateUrl: './reply-box.component.html',
  styleUrls: ['./reply-box.component.css']
})
export class ReplyBoxComponent implements OnInit {
  showReplyBox: boolean = false;
  replyText: string;

  @Input() parent;
  @Input() postId;
  @Input() commentsContainer;

  constructor(private commentService: CommentService) { }

  ngOnInit() {
  }

  openReplyBox() {
    this.showReplyBox = true;
  }

  createChildComment() {
    this.commentService.createComment(this.replyText, this.parent, this.postId)
      .then(this.handleCommentCreation.bind(this));
  }

  handleCommentCreation(newComment: Comment) {
    this.resetReplyBox();
    this.commentsContainer.push(newComment);
  }

  resetReplyBox() {
    this.showReplyBox = false;
    this.replyText = '';
  }
}
