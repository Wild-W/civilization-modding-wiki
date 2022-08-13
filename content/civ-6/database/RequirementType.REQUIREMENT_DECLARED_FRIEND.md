---
tags:
- RequirementType
title: REQUIREMENT_DECLARED_FRIEND
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_DECLARED_FRIEND
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_DECLARED_FRIEND"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_DECLARED_FRIEND",
		"REQUIREMENT_DECLARED_FRIEND"
	);


```
