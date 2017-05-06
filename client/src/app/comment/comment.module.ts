import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {CommentComponent} from './comment.component';
import {CommentService} from './comment.service';
import {ReplyBoxModule} from '../reply-box/reply-box.module';

@NgModule({
  imports: [
    CommonModule,
    ReplyBoxModule
  ],
  declarations: [
    CommentComponent
  ],
  exports: [
    CommentComponent
  ],
  providers: [
    CommentService
  ]
})
export class CommentModule { }
