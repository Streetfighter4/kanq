import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {CommentComponent} from './comment.component';
import {FormsModule} from '@angular/forms';
import {CommentService} from './comment.service';

@NgModule({
  imports: [
    CommonModule,
    FormsModule
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
