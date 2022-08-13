---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_MEETS_SCORE_THRESHOLD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_MEETS_SCORE_THRESHOLD
>
> * Class: `PLAYERS`
> * Arguments:
>	* ScoreLowestDifficulty `Integer`
>	* IncrementPerDifficulty `Integer`
>	* ExtraIncrementHighestDifficulty `Integer`

## Samples

```SQL {title="VICTORY_SCORE_PLAYER_EXCEEDS_SCORE_THRESHOLD"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"VICTORY_SCORE_PLAYER_EXCEEDS_SCORE_THRESHOLD",
		"REQUIREMENT_PLAYER_MEETS_SCORE_THRESHOLD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"VICTORY_SCORE_PLAYER_EXCEEDS_SCORE_THRESHOLD",
		"ExtraIncrementHighestDifficulty",
		0
	),
	(
		"VICTORY_SCORE_PLAYER_EXCEEDS_SCORE_THRESHOLD",
		"IncrementPerDifficulty",
		100
	),
	(
		"VICTORY_SCORE_PLAYER_EXCEEDS_SCORE_THRESHOLD",
		"ScoreLowestDifficulty",
		200
	);
	```
