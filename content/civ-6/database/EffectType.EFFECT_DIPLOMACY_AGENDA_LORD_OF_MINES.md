---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_LORD_OF_MINES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_LORD_OF_MINES
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomPercentage `Integer`
>	* BottomRankingDiploMod `Integer`
>	* HiddenAgenda `Boolean`
>	* StatementKey `String`
>	* TopPercentage `Integer`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_MONEY_GRUBBER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_MONEY_GRUBBER",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_LORD_OF_MINES",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_30_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_MONEY_GRUBBER",
		"BottomPercentage",
		30
	),
	(
		"AGENDA_MONEY_GRUBBER",
		"BottomRankingDiploMod",
		"-6"
	),
	(
		"AGENDA_MONEY_GRUBBER",
		"HiddenAgenda",
		1
	),
	(
		"AGENDA_MONEY_GRUBBER",
		"StatementKey",
		"AGENDA_LORD_OF_MINES_WARNING"
	),
	(
		"AGENDA_MONEY_GRUBBER",
		"TopPercentage",
		65
	),
	(
		"AGENDA_MONEY_GRUBBER",
		"TopRankingDiploMod",
		6
	);
	
```

