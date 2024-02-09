import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError } from 'rxjs';
import { Enigma } from 'src/app/Models/Enigma';
import { ErrorHandler} from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EnigmaServiceService {

  apiUrl="https://literate-space-yodel-g6pv9qp66gj29p96-8000.app.github.dev/api/anonymyze?input_text=";

  constructor(private http:HttpClient) {

   }

   sendPrompt(prompt:Enigma): Observable<Enigma> {
    
    console.log(prompt,this.apiUrl)
    return this.http.post<Enigma>(this.apiUrl, prompt)
  }
}