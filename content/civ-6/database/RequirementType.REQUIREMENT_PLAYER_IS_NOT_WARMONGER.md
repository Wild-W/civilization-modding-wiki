---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_NOT_WARMONGER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_NOT_WARMONGER
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_NOT_WARMONGER_SUBJECT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_NOT_WARMONGER_SUBJECT",
		"REQUIREMENT_PLAYER_IS_NOT_WARMONGER"
	);

```
