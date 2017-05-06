import {Component, Input, OnInit} from '@angular/core';
import {CommentService} from './comment.service';
import {Comment} from './comment';

@Component({
  selector: 'comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.css']
})
export class CommentComponent {
  @Input() comment: Comment;
}
