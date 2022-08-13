---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_FOUNDED_RELIGION_WITH_BELIEF
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_FOUNDED_RELIGION_WITH_BELIEF
>
> * Class: `PLAYERS`
> * Arguments:
>	* BeliefType `String`

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_PAPAL_PRIMACY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_PAPAL_PRIMACY",
		"REQUIREMENT_PLAYER_FOUNDED_RELIGION_WITH_BELIEF"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_PAPAL_PRIMACY",
		"BeliefType",
		"BELIEF_PAPAL_PRIMACY"
	);
	
```
