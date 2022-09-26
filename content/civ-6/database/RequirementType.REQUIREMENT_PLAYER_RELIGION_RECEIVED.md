---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_RELIGION_RECEIVED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_RELIGION_RECEIVED
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_RELIGION_RECEIVED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_RELIGION_RECEIVED",
		"REQUIREMENT_PLAYER_RELIGION_RECEIVED"
	);


```