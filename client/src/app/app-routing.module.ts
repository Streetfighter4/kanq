import {RouterModule, Routes} from '@angular/router';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {NgModule} from '@angular/core';
import {FacebookTokenHandlerComponent} from './oauth/facebook/facebook_token_handler.component';
import {DeviantArtAuthorizerComponent} from './oauth/deviant_art/deviant_art_authorizer.component';
import {DeviantArtTokenHandlerComponent} from './oauth/deviant_art/deviant_art_token_handler.component';

const routes: Routes = [
  {path: 'oauth/facebook/authorize', component: FacebookAuthorizerComponent},
  {path: 'oauth/facebook/token', component: FacebookTokenHandlerComponent},
  {path: 'oauth/deviant_art/authorize', component: DeviantArtAuthorizerComponent},
  {path: 'oauth/deviant_art/token', component: DeviantArtTokenHandlerComponent}
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
