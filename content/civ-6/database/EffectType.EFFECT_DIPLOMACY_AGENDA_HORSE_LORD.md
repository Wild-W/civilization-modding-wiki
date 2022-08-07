---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_HORSE_LORD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_HORSE_LORD
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomPercentage `Integer`
>	* BottomRankingDiploMod `Integer`
>	* PromotionClass1 `String`
>		* [UnitPromotionClasses.PromotionClassType]
>	* PromotionClass2 `String`
>		* [UnitPromotionClasses.PromotionClassType]
>	* StatementKey `String`
>	* TopPercentage `Integer`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_HORSE_LORD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_HORSE_LORD",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_HORSE_LORD",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_HORSE_LORD",
		"BottomPercentage",
		30
	),
	(
		"AGENDA_HORSE_LORD",
		"BottomRankingDiploMod",
		7
	),
	(
		"AGENDA_HORSE_LORD",
		"PromotionClass1",
		"PROMOTION_CLASS_HEAVY_CAVALRY"
	),
	(
		"AGENDA_HORSE_LORD",
		"PromotionClass2",
		"PROMOTION_CLASS_LIGHT_CAVALRY"
	),
	(
		"AGENDA_HORSE_LORD",
		"StatementKey",
		"AGENDA_HORSE_LORD_WARNING"
	),
	(
		"AGENDA_HORSE_LORD",
		"TopPercentage",
		70
	),
	(
		"AGENDA_HORSE_LORD",
		"TopRankingDiploMod",
		"-6"
	);
	
```

