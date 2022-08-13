---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_ERA_AGE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_ERA_AGE_MATCHES
>
> * Class: `PLAYERS`
> * Arguments:
>	* Type `String`
>		* DARK>		  GOLDEN>		  NONE

## Samples

```SQL {title="OPPONENT_IS_IN_GOLDEN_AGE_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"OPPONENT_IS_IN_GOLDEN_AGE_REQUIREMENT",
		"REQUIREMENT_OPPONENT_ERA_AGE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"OPPONENT_IS_IN_GOLDEN_AGE_REQUIREMENT",
		"Type",
		"GOLDEN"
	);
	
```
