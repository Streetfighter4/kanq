import {Component, Input, OnInit} from '@angular/core';
import {Comment} from './comment';

@Component({
  selector: 'comment',
  moduleId: module.id,
  templateUrl: 'comment.component.html',
  styleUrls: ['comment.component.css']
})
export class CommentComponent {
  @Input() comment: Comment;

  rate(value: number) {
    console.log('rated', value);
  }
}
