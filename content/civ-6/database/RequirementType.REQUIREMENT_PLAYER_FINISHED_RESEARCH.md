---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_FINISHED_RESEARCH
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_FINISHED_RESEARCH
>
> * Class: `PLAYERS`
> * Arguments:
>	* TechCivicDifferential `Integer`

## Samples

```SQL {title="REQUIRES_LAGS_PROGRESS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_LAGS_PROGRESS",
		"REQUIREMENT_PLAYER_FINISHED_RESEARCH"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_LAGS_PROGRESS",
		"TechCivicDifferential",
		"-3"
	);
	```
