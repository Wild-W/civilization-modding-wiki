---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_BUILT_WONDER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_BUILT_WONDER
>
> * Class: `PLAYERS`
> * Arguments:
>	* WonderRatio `Integer`

## Samples

```SQL {title="REQUIRES_LAGS_WONDERS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_LAGS_WONDERS",
		"REQUIREMENT_PLAYER_BUILT_WONDER"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_LAGS_WONDERS",
		"WonderRatio",
		"-1.2"
	);
	```
