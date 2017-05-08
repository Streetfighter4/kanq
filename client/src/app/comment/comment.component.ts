import {Component, Input, OnInit} from '@angular/core';
import {Comment} from './comment';
import {CommentService} from './comment.service';

@Component({
  selector: 'comment',
  moduleId: module.id,
  templateUrl: 'comment.component.html',
  styleUrls: ['comment.component.css']
})
export class CommentComponent {
  @Input() comment: Comment;

  constructor(private commentService: CommentService) { }

  rate(value: number) {
    this.commentService.rate(this.comment.id, value);
  }
}
