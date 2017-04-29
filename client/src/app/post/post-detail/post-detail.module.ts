import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {PostDetailComponent} from './post-detail.component';
import {PostService} from '../post.service';
import {CommentModule} from '../../comment/comment.module';
import {FormsModule} from '@angular/forms';

@NgModule({
  imports: [
    CommonModule,
    CommentModule,
    FormsModule
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
