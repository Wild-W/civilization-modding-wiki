---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_CONQUERING_ALLYING_MINORS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_CONQUERING_ALLYING_MINORS
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_CONQUERING_ALLYING_MINORS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CONQUERING_ALLYING_MINORS",
		"REQUIREMENT_PLAYER_CONQUERING_ALLYING_MINORS"
	);

```
