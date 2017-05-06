import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {PostDetailComponent} from './post-detail.component';
import {PostService} from '../post.service';
import {CommentModule} from '../../comment/comment.module';
import {ReplyBoxModule} from '../../reply-box/reply-box.module';

@NgModule({
  imports: [
    CommonModule,
    CommentModule,
    ReplyBoxModule
  ],
  declarations: [
    PostDetailComponent
  ],
  exports: [
    PostDetailComponent
  ],
  providers: [
    PostService
  ]
})
export class PostDetailModule { }
